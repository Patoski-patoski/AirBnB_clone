#!/usr/bin/env python3

"""review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review: inherits from Base Model"""

    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""
