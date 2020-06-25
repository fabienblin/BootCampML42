from book import Book
from recipe import Recipe

# The first french loving method cook book

mayo = Recipe("Mayo", 1, 1, ["egg", "mustard", "oil"],
              "fine mayones", "dessert")
oyster = Recipe("Oyster", 1, 1, ["oyster", "lemon"],
                "milky oysters", "starter")

book = Book("The Day After's reinvented wo.men")
book.add_recipe(mayo)
book.add_recipe(oyster)

print(mayo)
print(book.get_recipe_by_name("Oyster"))
