from Ingredient import Ingredient
from Recipe import Recipe
class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for x in scaled.ingredients:
            self._items.append((x, recipe.title))
    def remove_recipe(self, title: str):
        self._items = [x for x in self._items if x[1] != title]
    def get_list(self):
        s = {}
        result = []
        for x in self._items:
            key = (x[0].name, x[0].unit)
            if key not in s:
                s[key] = x[0].quantity
            else:
                s[key] += x[0].quantity
        for key in s:
            result.append(Ingredient(key[0],  s[key], key[1]))
        result.sort(key=lambda x: x.name)
        return result
    def __add__(self, other: ShoppingList):
        new = ShoppingList()
        new._items = self._items + other._items
        return new