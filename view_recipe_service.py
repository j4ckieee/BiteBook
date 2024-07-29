import time
import json
from prettytable import PrettyTable

while True:
    with open('view_recipe.txt', 'r') as idx_file:
        selected_index = idx_file.read()

    if selected_index.isdigit():
        selected_index = int(selected_index)
        print(f"Received index {selected_index}...")
        time.sleep(1)
        print("Finding recipe...")
        time.sleep(1)
        with open('catalog.txt', 'r') as file:
            recipe = json.load(file)
            if selected_index != 0 and selected_index <= len(recipe):
                name = recipe[selected_index - 1]["recipe_name"]
                description = recipe[selected_index - 1]["description"]
                ingredients = (recipe[selected_index - 1]["ingredients"])
                instructions = (recipe[selected_index - 1]["instructions"])

                # special formatting
                ingredients = ingredients.replace(',', '\n -')
                instructions = instructions.replace('.', '.\n')

                # display recipe
                recipe_table = PrettyTable(align="l")
                recipe_table.field_names = [name]
                # recipe_table.add_row([f'Recipe Name:\n{name}\n'])
                recipe_table.add_row([f'Description:\n{description}\n'])
                recipe_table.add_row([f'Ingredients:\n - {ingredients}\n'])
                recipe_table.add_row([f'Instructions:\n {instructions}'])
                recipe_table = recipe_table
                #print(recipe_table, "\n")

            print(f'Submitting {name} recipe...')
            time.sleep(1)

        with open('view_recipe.txt', 'w+') as file:
            file.write(recipe_table.get_string())
            #json.dump(recipe_table.get_json_string())

            #file.write(recipe_table.get_json_string())

