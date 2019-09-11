

import math

def recipe_batches(recipe, ingredients):

  possible_amounts_of_batches = []

  max_batches_possible = 1
  
  for key in recipe:
    if recipe[key] > ingredients[key]:
      max_batches_possible = 0
      
  
  if max_batches_possible == 0:
    return ( max_batches_possible)
  
  if max_batches_possible != 0:

    for key in recipe:

      left_batches = ingredients[key] // recipe[key]
      possible_amounts_of_batches.append(left_batches)

      for j in range(1, len(possible_amounts_of_batches)):
        if possible_amounts_of_batches[j] <= possible_amounts_of_batches[j-1]:
          max_batches_possible = possible_amounts_of_batches[j-1]

    return( max_batches_possible )

print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 18, 'butter': 102, 'flour': 51 }
))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))