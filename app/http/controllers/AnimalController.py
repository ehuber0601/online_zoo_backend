""" A AnimalController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Animal import Animal


class AnimalController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        id = self.request.param("id")
        return Animal.where("id", id).get()
        

    def index(self):
        return Animal.all()

    def create(self):
        name = self.request.input("name")
        scientific_name = self.request.input("scientific name")
        url = self.request.input("url")
        animal_class = self.request.input("class")
        lifespan = self.request.input("lifespan")
        origin = self.request.input("origin")
        fun_fact = self.request.input("fun fact")
        animal = Animal.create({"name": name, "scientific name": scientific_name, "url": url, "class": animal_class, "lifespan": lifespan, "origin": origin, "fun fact": fun_fact})
        return animal


    def update(self):
        id = self.request.param("id")
        name = self.request.input("name")
        scientific_name = self.request.input("scientific name")
        url = self.request.input("url")
        animal_class = self.request.input("class")
        lifespan = self.request.input("lifespan")
        origin = self.request.input("origin")
        fun_fact = self.request.input("fun fact")
        Animal.where("id", id).update({"name": name, "scientific name": scientific_name, "url": url, "class": animal_class, "lifespan": lifespan, "origin": origin, "fun fact": fun_fact})
        return Animal.where("id", id).get()


    def destroy(self):
        id = self.request.param("id")
        animal = Animal.where("id", id).get()
        Animal.where("id", id).delete()
        return animal