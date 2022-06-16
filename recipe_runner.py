import pprint as pp
import ast

lowest_score_recipes = {}

recipes = {
	'Baked Stuffed Fish with Turmeric Rice': {
		'source': 'Piquant Post',
		'serves': 4,
		'prep_time_min': 20,
		'cook_time_min': 30,
		'total_time_min': 50,
		'ingredients': {
			'yellow onion': {
				'amount': .5,
				'unit': 'whole'
				}
			,'raw walnuts': {
				'amount': 1,
				'unit': 'cup'
				}
			,'fresh pomegranate seeds': {
				'amount': .66,
				'unit': 'cup'
				}
		},
		'temp_recipe_score': 0
	},
	'Ice Cream Sundae': {
		'source': 'Homemade',
		'serves': 1,
		'prep_time_min': 2,
		'cook_time_min': 0,
		'total_time_min': 2,
		'ingredients': {
			'vanilla ice cream': {
				'amount': 3,
				'unit': 'scoop'
				}
			,'chocolate syrup': {
				'amount': 8,
				'unit': 'ounce'
				}
		},
		'temp_recipe_score': 0
	},
	'PB&J': {
		'source': 'Homemade',
		'serves': 1,
		'prep_time_min': 2,
		'cook_time_min': 0,
		'total_time_min': 2,
		'ingredients': {
			'bread': {
				'amount': 2,
				'unit': 'slice'
				}
			,'jelly': {
				'amount': 4,
				'unit': 'ounce'
				}	
			,'peanut butter': {
				'amount': 4,
				'unit': 'ounce'
			}		
		},
		'temp_recipe_score': 0
	}
}

ingredients_owned = {'vanilla ice cream': {
						'amount': 3,
						'unit': 'scoop'
						}
					,'jelly': {
						'amount': 8,
						'unit': 'ounce'
						}
					,'bread': {
						'amount': 12,
						'unit': 'slice'
						}
					}
ingredients_needed = {}

for rec in recipes:
	print(rec)
	for rec_ing in recipes[rec]['ingredients']:
		
		if rec_ing not in ingredients_owned.keys():
			recipes[rec]['temp_recipe_score'] += 1

		elif ingredients_owned[rec_ing]['amount'] < recipes[rec]['ingredients'][rec_ing]['amount']:
			recipes[rec]['temp_recipe_score'] += 1
		
		else:
			pass

	if lowest_score_recipes == {}:
		lowest_score_recipes['%i' % recipes[rec]['temp_recipe_score']] = [rec] 
		print(type(lowest_score_recipes['%i' % recipes[rec]['temp_recipe_score']]))

	elif int(list(lowest_score_recipes.keys())[0]) == recipes[rec]['temp_recipe_score']: 
		lowest_score_recipes[int('%i' % (recipes[rec]['temp_recipe_score']))].append(recipes[rec]['temp_recipe_score'])

	elif int(list(lowest_score_recipes.keys())[0]) > recipes[rec]['temp_recipe_score']: 
		lowest_score_recipes = ast.literal_eval(("{%i : '%s'}" % (recipes[rec]['temp_recipe_score'],rec)))

		### ONE HOUR SPENT ON THE BELOW ALTERNATIVE... ###
		# lowest_score_recipes = ast.literal_eval(("{'{0}'':''{1}'}").format(recipes[rec]['temp_recipe_score'],rec))
	else:
		pass

pp.pp(recipes)
pp.pp(lowest_score_recipes)