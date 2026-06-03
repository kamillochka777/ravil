class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, f_quantity):
        f_quantity = float(f_quantity)
        if f_quantity <= 0:
            raise ValueError('Колтчество должно быть положительным')
        self._quantity = f_quantity
    def __str__(self):
        return f'{self.name.capitalize()}: {self.quantity} {self.unit}'
    def __repr__(self):
        return f"Ingredient('{self.name.capitalize()}', {self.quantity}, '{self.unit}')"
    def __eq__(self, ingredient2):
        return self.name == ingredient2.name and self.unit == ingredient2.unit
    