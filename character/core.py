# -*- coding: utf-8 -*-
from . import defaults

class Character:
  def __init__(self, name):
    self.name = name
    self.attributes = defaults.attributes
    self.skills = defaults.skills

  def print_attributes(self):
    print(', '.join([f"{key}: d{self.attributes[key]}" for key in self.attributes]))

  def print_skills(self):
    print(', '.join([f"{key}: d{self.skills[key]}" for key in self.skills]))

  # Default function when class is called
  # Maybe eventually use to return JSON object for??
  def __repr__(self):
    return self.name
