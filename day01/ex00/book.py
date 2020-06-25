import datetime
import recipe


class Book:
    def __init__(self, name=None, last_update=datetime.datetime.today(),
                 creation_date=datetime.datetime.today()):
        self.name = ""
        self.last_update = None
        self.creation_date = None
        self.recipe_list: dict = {"starter": [], "lunch": [], "dessert": []}

        if name is None\
           or type(name) is not str\
           or name == "":
            print("Invalid book name.")
            exit(1)
        else:
            self.name = name

        if not isinstance(last_update.__class__, datetime.datetime.__class__):
            print("Invalid update datetime.")
            exit(1)
        else:
            self.last_update = last_update

        if not isinstance(creation_date.__class__,
           datetime.datetime.__class__):
            print("Invalid creation datetime.")
            exit(1)
        else:
            self.creation_date = creation_date

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` nad return the instance"""
        pass
        if type(name) is not str:
            print(name, "is not in the recipe list.")
        else:
            for r_type in self.recipe_list:
                for r in self.recipe_list[r_type]:
                    if r.name == name:
                        return r

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        pass
        if type(recipe_type) is not str:
            print("Invalid recipe type name.")
        else:
            return self.recipe_list[recipe_type]

    def add_recipe(self, recipe: recipe.Recipe):
        """Add a recipe to the book and update last_update"""
        pass
        if type(recipe) is not recipe.__class__:
            print("Invalid recipe type.")
        else:
            r_type = recipe.recipe_type
            recipe_lst = self.get_recipes_by_types(r_type)
            if recipe not in recipe_lst:
                recipe_lst.append(recipe)
