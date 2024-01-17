#!/usr/bin/env python3

"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
