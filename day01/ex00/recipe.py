class Recipe:
    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, description=None, recipe_type=None):
        self.name = ""
        self.cooking_lvl = 0
        self.cooking_time = 0
        self.ingredients = [""]
        self.description = ""
        self.recipe_type = ""

        if name is None\
           or type(name) is not str\
           or name == "":
            print("Invalid recipe name.")
            exit(1)
        else:
            self.name = name

        if cooking_lvl is None\
           or type(cooking_lvl) is not int\
           or cooking_lvl <= 0 or cooking_lvl >= 6:
            print("Invalid cooking level.")
            exit(1)
        else:
            self.cooking_lvl = cooking_lvl

        if cooking_time is None\
           or type(cooking_time) is not int\
           or cooking_time < 0:
            print("Invalid cooking time.")
            exit(1)
        else:
            self.cooking_time = cooking_time

        if ingredients is None\
           or type(ingredients) is not list\
           or not all(isinstance(ingr, str) for ingr in ingredients)\
           or len(ingredients) == 0:
            print("Invalid ingredient list.")
            exit(1)
        else:
            self.ingredients = ingredients

        if description is not None\
           and type(description) is not str:
            print("Invalid description.")
            exit(1)
        else:
            self.description = description

        if recipe_type is None\
           or type(recipe_type) is not str\
           or recipe_type not in ["starter", "lunch", "dessert"]:
            print("Invalid recipe type.")
            exit(1)
        else:
            self.recipe_type = recipe_type

    def __str__(self):
        txt = "\
               Recipe for {0.name}\n\
               Difficulty: {0.cooking_lvl}\n\
               Time: {0.cooking_time}\n\
               Ingredients: {0.ingredients}\n\
               Description: {0.description}\n\
               Type: {0.recipe_type}\
              ".format(self)
        return txt
