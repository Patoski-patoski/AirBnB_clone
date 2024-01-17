#!/usr/bin/env python3

"""place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place: inherits from Base Model"""

    name = ""
    state_id = ""
    user_id = ""  # string - empty string: it will be the User.id
    city_id = ""  # string - empty string: it will be the City.id
    description = ""
    max_guest = 0
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = ""  # list of string: it'll be the list of Amenity.id later
