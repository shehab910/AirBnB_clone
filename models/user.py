#!/usr/bin/python3
"""This module contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
  """This class defines a user by various attributes"""
  email = ""
  password = ""
  first_name = ""
  last_name = ""

  def __init__(self, *args, **kwargs):
    """Initializes a user"""
    super().__init__(*args, **kwargs)
