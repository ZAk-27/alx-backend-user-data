#!/usr/bin/env python3
"""
Defining a SessionAuth class 
"""
import uuid
from typing import (
    TypeVar,
    Union
)
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Authentication class implement
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Union[str, None]:
        """
        session id from random string
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(
        self, session_id: str = None
    ) -> Union[str, None]:
        """
        Get user id
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> Union[TypeVar('User'), None]:
        """
        current authenticated logged in user
        """
        User.load_from_file()
        return User.get(
            self.user_id_for_session_id(self.session_cookie(request))
        )

    def destroy_session(self, request=None) -> bool:
        """
        logout
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
