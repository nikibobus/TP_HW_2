from Ingredient import Ingredient
class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is not None:
            self.ingredients = ingredients
        else:
            self.ingredients = []
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except (TypeError, ValueError):
            return False
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должен быть положительным числом")
        new_ingredients = []
        for x in self.ingredients:
            new_ingredients.append(Ingredient(x.name, x.quantity * ratio, x.unit))
        return Recipe(self.title, new_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        result = ''
        for x in self.ingredients:
            result += str(x) + '\n'
        return str(self.title) + '\n' + result
