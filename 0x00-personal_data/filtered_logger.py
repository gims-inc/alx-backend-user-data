#!/usr/bin/env python3
"""Handling of personal data"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns an obfuscated log message"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message