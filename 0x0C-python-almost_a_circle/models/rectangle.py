#!/usr/bin/python3
"""
Module contains a class Rectangle
inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """define a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
