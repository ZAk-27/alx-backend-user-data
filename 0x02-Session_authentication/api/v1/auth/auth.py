#!/usr/bin/env python3
"""
A module: Defines an template class defining
for all authentication system 
"""
import os
from flask import request

from typing import (
    List,
    TypeVar,
    Union
)


class Auth:
    """
    API authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        authentication request
        """
        if (
            path is None
            or excluded_paths is None
            or len(excluded_paths) == 0
        ):
            return True
        for url in excluded_paths:
            if url.endswith('*'):
                if url[:-1] in path:
                    return False
            else:
                if path in url or path + '/' in url:
                    return False
        return True

    def authorization_header(self, request=None) -> Union[str, None]:
        """
        documentation
        """
        auth = request.headers.get('Authorization', None) if request else None
        if request is None or auth is None:
            return None
        return auth

    def current_user(self, request=None) -> Union[TypeVar('User'), None]:
        """
        documentation
        """
        return None

    def session_cookie(self, request=None) -> Union[str, None]:
        """
        documentation
        """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
