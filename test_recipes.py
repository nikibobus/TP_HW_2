import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from DietaryRecipe import DietaryRecipe
from ShoppingList import ShoppingList
def test_ingredient_creation():
    ingredient = Ingredient('Говядина', 5000, 'кг')
    assert ingredient.name == 'Говядина'
    assert ingredient.quantity == 5000.0
    assert ingredient.unit == 'кг'
    
def test_ingredient_str():
    ingredient = Ingredient('Мука', 500, 'г')
    assert str(ingredient) == 'Мука: 500.0 г'

def test_ingredient_eq_same():
    ingredient_1 = Ingredient("Гавядина", 1000, "кг")
    ingredient_2 = Ingredient("Гавядина", 1, "кг")
    assert ingredient_1 == ingredient_2

def test_ingredient_eq_different_name():
    ingredient_1 = Ingredient("Гавядина", 1000, "кг")
    ingredient_2 = Ingredient("Курица", 1000, "кг")
    assert ingredient_1 != ingredient_2

def test_ingredient_eq_different_unit():
    ingredient_1 = Ingredient("Гавядина", 1000, "кг")
    ingredient_2 = Ingredient("Гавядина", 1000, "столовых ложек")
    assert ingredient_1 != ingredient_2

def test_recipe_creation():
    ingredients_1 = Ingredient('Мука', 500, 'г')
    ingredients_2 = Ingredient('Яйцо', 2, 'шт')
    recipe = Recipe('Блины', [ingredients_1, ingredients_2])
    assert recipe.title == 'Блины'
    assert recipe.ingredients == [ingredients_1, ingredients_2]

def test_recipe_add_ingredient():
    recipe = Recipe('Блины')
    ingredients_1 = Ingredient('Мука', 500, 'г')
    recipe.add_ingredient(ingredients_1)
    assert ingredients_1 in recipe.ingredients
    ingredients_2 = Ingredient('Мука', 200, 'г')
    recipe.add_ingredient(ingredients_2)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 700.0

def test_recipe_scale():
    ingredients_1 = Ingredient('Мука', 500, 'г')
    recipe = Recipe('Блины', [ingredients_1])
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert recipe.ingredients[0].quantity == 500.0
    assert scaled.ingredients[0].quantity == 1000.0
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_recipe_len():
    recipe = Recipe('Блины')
    assert len(recipe) == 0
    recipe.add_ingredient(Ingredient('Мука', 500, 'г'))
    recipe.add_ingredient(Ingredient('Яйцо', 2, 'шт'))
    assert len(recipe) == 2

def test_shopping_list_add_recipe():
    recipe = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe, 2)
    assert len(shop_list._items) == 1
    assert shop_list._items[0][0].name == 'Мука'
    assert shop_list._items[0][0].quantity == 1000.0
    with pytest.raises(ValueError):
        shop_list.add_recipe(recipe, 0)
    with pytest.raises(ValueError):
        shop_list.add_recipe(recipe, -1)

def test_shopping_list_remove_recipe():
    recipe_1 = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    recipe_2 = Recipe('Омлет', [Ingredient('Яйцо', 3, 'шт')])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe_1, 1)
    shop_list.add_recipe(recipe_2, 1)
    shop_list.remove_recipe('Блины')
    assert len(shop_list._items) == 1
    assert shop_list._items[0][1] == 'Омлет'
    shop_list.remove_recipe('Гавядина')
    assert len(shop_list._items) == 1

def test_shopping_list_get_list():
    recipe1 = Recipe('Блины', [Ingredient('Мука', 500, 'г'), Ingredient('Яйцо', 2, 'шт')])
    recipe2 = Recipe('Кекс', [Ingredient('Мука', 200, 'г'), Ingredient('Сахар', 100, 'г')])
    shop_list = ShoppingList()
    shop_list.add_recipe(recipe1, 2)
    shop_list.add_recipe(recipe2, 1)
    res = shop_list.get_list()
    assert len(res) == 3
    assert res[0].name == 'Мука'
    assert res[0].quantity == 1200.0
    assert res[1].name == 'Сахар'
    assert res[1].quantity == 100.0
    assert res[2].name == 'Яйцо'
    assert res[2].quantity == 4.0

def test_shopping_list_add_operator():
    recipe_1 = Recipe('Блины', [Ingredient('Мука', 500, 'г')])
    recipe_2 = Recipe('Омлет', [Ingredient('Яйцо', 3, 'шт')])
    list1 = ShoppingList()
    list1.add_recipe(recipe_1, 1)
    list2 = ShoppingList()
    list2.add_recipe(recipe_2, 1)
    combined = list1 + list2
    assert len(combined._items) == 2
    assert len(list1._items) == 1
    assert len(list2._items) == 1
