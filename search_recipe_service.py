import zmq
import time
import json
from prettytable import PrettyTable

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4686")

while True:
    #  Wait for request from client
    print("Waiting for request...")
    req_recipe = socket.recv_string()

    #  Received request
    print(f"Received request for {req_recipe}")
    time.sleep(1)

    # Open catalog and search for recipe
    with open('catalog.txt', 'r+') as file:
        all_recipes = json.load(file)
        result = "Sorry - Recipe not found."
        for idx, recipe in enumerate(all_recipes, 0):
            curr_recipe = all_recipes[idx]["recipe_name"]
            curr_recipe = str(curr_recipe).lower()

            # Recipe found - format into table
            if curr_recipe == req_recipe:
                print("Recipe Found!")
                found_recipe = all_recipes[idx]

                name = all_recipes[idx]["recipe_name"]
                description = all_recipes[idx]["description"]
                ingredients = all_recipes[idx]["ingredients"]
                instructions = all_recipes[idx]["instructions"]

                # special formatting
                ingredients = ingredients.replace(',', '\n -')
                instructions = instructions.replace('.', '.\n')

                # display recipe
                recipe_table = PrettyTable(align="l")
                recipe_table.field_names = [name]

                recipe_table.add_row([f'Description:\n{description}\n'])
                recipe_table.add_row([f'Ingredients:\n - {ingredients}\n'])
                recipe_table.add_row([f'Instructions:\n {instructions}'])
                result = recipe_table.get_string()
                print(result)
                break

    # Send back response
    socket.send_string(result)


