#!/usr/bin/env python3
"""Handling of personal data  --encryption"""

import bcrypt


def hash_password(password: str) -> bytes:
    """function that expects one string argument name password and returns
    a salted,hashed password, which is a byte string.
    args:
        pasword: (str)
        returns: hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password matches the hashed password.
    args:
        hashed_password: (bytes) hashed password
        password: (str) provided password
        returns: bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
