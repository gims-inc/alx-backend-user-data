#!/usr/bin/env python3
""" Module for authentication
"""
from flask import request
from typing import List, TypeVarTuple
import re


class Auth():
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication
        args:
            path (str)
            excluded_paths (List(str))
        returns:
            False - path and excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
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

    def current_user(self, request=None) -> TypeVarTuple('User'):
        """Current user function
        args:
            request
        returns:
            returns None - request
        """
        return None
