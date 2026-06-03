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
        