class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.dietary_info = diet_type
    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)
    def __str__(self):
        return '[' + str(self.dietary_info) + ']' + super().__str__() 