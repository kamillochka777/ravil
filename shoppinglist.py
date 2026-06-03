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
    def get_list(self):
        itog = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in itog:
                itog[key] += ingredient.quantity
            else:
                itog[key] = ingredient.quantity
        spisok = []
        for (name, unit), quantity in itog.items():
            name_1 = name
            spisok.append(Ingredient(name_1, quantity, unit))
        spisok.sort(key = lambda i: i.name)
        return spisok
    def __add__(self, other):
        new_spisok = ShoppingList()
        for ingredient, title in self._items:
            new_spisok._items.append((ingredient, title))
        for ingredient, title in other._item:
            new_spisok._items.append((ingredient, title))
        return new_spisok