"""CreateAnimalTable Migration."""

from masoniteorm.migrations import Migration


class CreateAnimalTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("animals") as table:
            table.increments("id")
            table.string("name")
            table.string("scientific name")
            table.string("url")
            table.string("class")
            table.string("lifespan")
            table.string("origin")
            table.string("fun fact")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("animals")
