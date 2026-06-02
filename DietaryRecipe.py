from Recipe import Recipe
from Ingredient import Ingredient
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)
    def __str__(self):
        return '[' + str(self.diet_type) + '] ' + super().__str__() 
