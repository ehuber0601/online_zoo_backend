"""AnimalTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Animal import Animal


class AnimalTableSeeder(Seeder):
    def run(self):
        Animal.create({"name": "Northern Giraffe", "scientific_name": "Giraffa camelopardalis", "url": "https://giraffeconservation.org/wp-content/uploads/2019/03/northern-giraffe_gcf_stock-24.jpg", "class": "mammal", "lifespan": "~26 years", "origin": "Africa", "fun_fact": "Tallest mammal on Earth"})
        Animal.create({"name": "African elephant", "scientific_name": "Loxodonta", "url": "https://cdn.mos.cms.futurecdn.net/rvFpfXVchpZPrtBh8NWAX6-1200-80.jpg", "class": "mammal", "lifespan": "60-70 years", "origin": "Africa", "fun_fact": "Largest Land Animal"})
        Animal.create({"name": "Bengal Tiger", "scientific_name": "Panthera Tigris Tigris", "url": "https://www.tigers-world.com/wp-content/uploads/Bengal.jpg", "class": "mammal", "lifespan": "~11 years", "origin": "Asia", "fun_fact": "Are amazing swimmers"})
