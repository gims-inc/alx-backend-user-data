#!/usr/bin/env python3
""" Module for authentication
"""
from flask import request
from typing import List, TypeVar
import re


class Auth():
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a path requires authentication
        args:
            path (str)
            excluded_paths (List(str))
        returns:
            False - path and excluded_paths
        """
        if not path:
            return True
        if not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/').startswith(excluded_path.rstrip('/')):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorisation_header function
        args:
            request
        returns:
            returns None - request
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user function
        args:
            request
        returns:
            returns None - request
        """
        return None
