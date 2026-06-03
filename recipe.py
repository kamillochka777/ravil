class Recipe():
    def __init__(self, title, ingredients):
        self.title = title
        self._ingredients = []
        for ingr in ingredients:
            self.add_ingredient(ingr)
    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self._ingredients:
            if ingr.name == ingredient.name and ingr.unit == ingredient.unit:
                ingr.quantity = ingr.quantity + ingredient.quantity
                return
            self._ingredients.append(ingredient)
    