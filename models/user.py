#!/usr/bin/python3
"""This module creates a User Class"""

from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    