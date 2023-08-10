#!/usr/bin/python3
"""
This module carries the base model for the entire AIRBNB Project
"""

from uuid import uuid4
from _datetime import datetime
import models


class BaseModel:
    """
    This is the base class for the entire AirBnb project
    """
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        This method initializes the instance with the specific
        variables that are specified
        """
        if len(kwargs) > 0:
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], BaseModel.DATE_FORMAT)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], BaseModel.DATE_FORMAT)
            if "__class__" in kwargs:
                kwargs.pop("__class__")

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        :return: Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        my_dict = {
            "__class__": self.__class__.__name__
        }

        for (k, v) in self.__dict__.items():
            if k == "created_at":
                v = v.strftime(BaseModel.DATE_FORMAT)
                my_dict[k] = v
            elif k == "updated_at" and type(v) == "datetime.datetime":
                v = v.strftime(BaseModel.DATE_FORMAT)
                my_dict[k] = v
            else:
                my_dict[k] = v

        return my_dict
