"""
Module for defining Pydantic models related to user management.

Includes Gender and Role enumerations along with a Pydantic User model.
"""
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


# Definition of an enumeration for gender
class Gender(str, Enum):
    """
    Enumeration for representing gender.

    Attributes:
    - male (str): Represents the male gender.
    - female (str): Represents the female gender.
    """
    MALE = "male"
    FEMALE = "female"

# Definition of an enumeration for user roles
class Role(str, Enum):
    """
    Enumeration for representing user roles.

    Attributes:
    - ADMIN (str): Represents the admin role.
    - USER (str): Represents the user role.
    """
    ADMIN = "admin"
    USER = "user"

# Definition of a Pydantic base class for user objects
class User(BaseModel):
    """
    Pydantic base class for modeling user objects.

    Attributes:
    - id (Optional[UUID]): The unique user identifier (UUID). Optional, defaults to a random UUID.
    - first_name (str): The user's first name.
    - last_name (str): The user's last name.
    - gender (Gender): The user's gender, defined by the Gender enumeration.
    - roles (List[Role]): A list of roles the user has, defined by the Role enumeration.
    """
    id: Optional[UUID] = uuid4()  # Generate a random UUID by default, optional
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]


class UpdateUser(BaseModel):
    """
    Pydantic model for updating user information.

    Attributes:
    - first_name (Optional[str]): The optional updated first name of the user.
    - last_name (Optional[str]): The optional updated last name of the user.
    - roles (Optional[List[Role]]): The optional updated list of roles for the user.
    """
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]
