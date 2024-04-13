#!/usr/bin/env python3
"""A module documntation.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """a module documntation.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """a module documntation.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
