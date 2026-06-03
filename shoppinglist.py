class ShoppingList():
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError('Количество порций должно быть положительным')
        sc_recipe = recipe.scale(portions)
        for ingredient in sc_recipe._ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]
        