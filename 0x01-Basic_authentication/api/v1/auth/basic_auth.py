#!/usr/bin/env python3
"""Basic Auth implimentation module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Method that returns the Base64 part of the Authorization header
        for a Basic Authentication:
        Args:
            authorization_header (str)
        Returns:
            None if authorization_header is None
            None if authorization_header is not a string
            None if authorization_header doesn't start by Basic
            (with a space at the end)
            Otherwise, return the value after Basic (after the space)
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user and password from the decoded Base64 string
        Args:
            decoded_base64_authorization_header (str)
        Returns:
            None, None if decoded_base64_authorization_header is None
            None if decoded_base64_authorization_header is not a string
            None if decoded_base64_authorization_header doesn’t contain :
            user email and the user password separated by a :
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return decoded_base64_authorization_header.split(':')

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Returns a User object from the user_email and user_pwd
        Args:
            user_email (str)
            user_pwd (str)
        Returns:
            None if user_email is None or not a string.
            None if user_pwd is None or not a string.
            None if your database (file) doesn’t contain any.
                User instance with email equal to user_email  all cases.
            None if user_pwd is not the password of the User instance found.
            Otherwise, return the User instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User.search({'email': user_email})
        if not user or len(user) == 0:
            return None
        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the User instance for a request.
        """
        auth_header = self.authorization_header(request)
        authorization = self.extract_base64_authorization_header(auth_header)
        _decode = self.decode_base64_authorization_header(authorization)
        credential = self.extract_user_credentials(_decode)
        return self.user_object_from_credentials(credential[0], credential[1])
