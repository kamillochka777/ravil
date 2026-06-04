class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        super().__init__(title, ingredients if ingredients is not None else [])
        self.diet_type = diet_type