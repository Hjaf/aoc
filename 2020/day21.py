import re
recipies = open('day21inputsample.txt', 'r').readlines()

recipe_book = {}
i = 0
for recipe in recipies:
    allergens = recipe.replace('\n', '').split('(contains ')[1][:-1].split(' ')
    ingredients = recipe.split('(contains ')[0].split(' ')
    # print('ingredients: %s with alergens: %s' %(ingredients, allergens))
    recipe_book[i] = {'ingredients': ingredients, 'allergens':allergens}
    i += 1

print(recipe_book)
   
for recipe in recipe_book:
    for allergen in recipe_book[recipe]['allergens']:
        for recipe_two in recipe_book:
            if allergen in recipe_book[recipe_two]['allergens']:
                print(recipe_book[recipe_two]['ingredients'])
