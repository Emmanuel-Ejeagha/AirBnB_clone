#!/usr/bin/python3
"""This is the module for Base_model class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is class for base model of object hierarchy"""

    def __init__(self, *args, **kwargs):
        """Initialization of Base instance.

        Args:
            *args: list of arguments
            **Kwargs: dict of keyword arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """This updates the updates_at attribute
        with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """This function returns a human-readable string
        representation of an instance"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my.dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict