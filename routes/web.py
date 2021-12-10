"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/", "AnimalController@index").name("index"),
        Get("/@id", "AnimalController@show").name("show"),
        Post("/", "AnimalController@create").name("create"),
        Put("/@id", "AnimalController@update").name("update"),
        Delete("/@id", "AnimalController@destroy").name("destroy")
    ], prefix="/animals", name="animals")
]
