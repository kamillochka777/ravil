class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        super().__init__(title, ingredients if ingredients is not None else [])
        self.diet_type = diet_type
    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled._ingredients)
    def __str__(self):
        return f'[{self.diet_type}] {self.title}'
    