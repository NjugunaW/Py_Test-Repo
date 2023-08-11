#!/usr/bin/python3
"""
This module defines a City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This module represents a City class

    Args:
        state_id (str):
        name (str):
    """
    state_id = ""
    name = ""
