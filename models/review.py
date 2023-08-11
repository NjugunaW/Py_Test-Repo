#!/usr/bin/python3
"""
This module defines a Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This module represents a Review class

    Args:
        place_id (str):
        user_id(str):
        text (str):
    """

    place_id = ""
    user_id = ""
    text = ""
