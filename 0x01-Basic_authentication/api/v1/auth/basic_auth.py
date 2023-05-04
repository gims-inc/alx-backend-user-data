#!/usr/bin/env python3
"""Basic Auth implimentation module
"""
from api.v1.auth.auth import Auth
import base64

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
            None if authorization_header doesn’t start by Basic
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
