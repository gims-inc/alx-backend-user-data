#!/usr/bin/env python3
"""Session Auth implimentation module
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """class SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates session-id for a user-id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user_id for a session_id
        """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """returns a user based on a cookie value
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """destroy session to logout"""
        if not request or not self.session_cookie(request):
            return False
        session_id = self.session_cookie(request)
        if not self.user_id_by_session_id.get(session_id):
            return False
        else:
            del self.user_id_by_session_id[session_id]
            return True
