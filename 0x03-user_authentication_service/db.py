#!/usr/bin/env python3
"""DB module implementaion
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound


from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Returns a User object. Saves the user to the database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Returns the first row found in the users table as filtered by the
        method’s input arguments
        """
        try:
            user = self.__session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """method that takes as argument a required user_id integer
        and arbitrary keyword arguments, and returns None.
        """
        # self.__session.query(User).filter_by(id=user_id).update(kwargs)
        user = self.find_user_by(id=user_id)
        user_properties = [column.name for column in User.__table__.columns]

        for key, val in kwargs.items():
            if key not in user_properties:
                raise ValueError
            setattr(user, key, val)

        self.__session.commit()
        return None
