#!/usr/bin/python3
"""This module is for user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a User"""
    email = ""
    password = ""
    first_name =""
    last_name = ""
