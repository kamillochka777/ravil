class Recipe():
    def __init__(self, title, ingredients):
        self.title = title
        self._ingredients = []
        for ingr in ingredients:
            self.add_ingredient(ingr)