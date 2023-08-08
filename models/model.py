#!/usr/bin/python3
"""
This module carries the base model for the entire AIRBNB Project
"""

from uuid import uuid4
from _datetime import datetime


class BaseModel:
    """
    This is the base class for the entire AirBnb project
    """

    def __init__(self):
        """
        This method initializes the instance with the specific
        variables that are specified
        """
        self.id = str(uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """
        This method returns the printable output for the class
        :return:
        """
        return f"[{BaseModel.__name__}]({self.id})<{self.__dict__}>"

    def save(self):
        """
        This method updates the current time to the updated_at attribute
        :return:
        """
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """
        :return: Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        my_dict = {
            "__class__": BaseModel.__name__
        }

        for (k, v) in self.__dict__.items():
            my_dict[k] = v

        return my_dict
