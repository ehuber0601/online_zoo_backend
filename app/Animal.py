"""Animal Model."""

from masoniteorm.models import Model


class Animal(Model):
    __table__="animals"