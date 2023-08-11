#!/usr/bin/python3
"""
This module defines a class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This module represents a user entity with attributes

    Args:
        email (str):
        password (str):
        first_name (str):
        last_name (str):
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
