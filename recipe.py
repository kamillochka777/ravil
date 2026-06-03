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
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0:
    def scale(self, ratio: ratio):
        scaled = []
        for ingr in self._ingredients:
            sc_quantity = ingr.quantity * ratio
            scaled.append(Ingredient(ingr.name, sc_quantity, ingr.unit))
        return Recipe(self.title, scaled)
    def __len__(self):
        return len(self._ingredients)
    def __str__(self):
        chitaemo = f'Блюдо: {self.title}\nИнгредиенты:'
        for ingr in self._ingredients:
            if ingr == self._ingredients[-1]:
                chitaemo += f' {ingr}'
            else:
                chitaemo += f' {ingr};'
        return chitaemo