#!/usr/bin/python3
"""This module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a review by various attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a review"""
        super().__init__(*args, **kwargs)
        # self.place_id = kwargs.get("place_id", "")
        # self.user_id = kwargs.get("user_id", "")
        # self.text = kwargs.get("text", "")
