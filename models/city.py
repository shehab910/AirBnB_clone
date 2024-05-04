#!/usr/bin/python3
"""This module contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a city by various attributes"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a city"""
        super().__init__(*args, **kwargs)
