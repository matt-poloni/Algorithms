#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    keys = [*recipe.keys()]
    k0 = keys[0]
    try:
        low = ingredients[k0] // recipe[k0]
    except:
        return 0
    for k in keys[1:]:
        rec = recipe[k]
        try:
            ing = ingredients[k]
        except:
            return 0
        if (batches := ing // rec) < low:
            low = batches
    return low

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))