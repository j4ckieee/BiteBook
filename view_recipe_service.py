import zmq
import time
import json
from prettytable import PrettyTable
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4682")

while True:
    #  Wait for request from client
    print("Waiting for request...")
    selected_index = socket.recv_json()

    # Received request
    selected_index = int(selected_index)
    print(f"Received index {selected_index}...")

    # Open catalog and search for matching index
    print("Finding recipe...")
    time.sleep(1)
    result = "Index does not exist in catalog."
    with open('catalog.txt', 'r') as file:
        recipe = json.load(file)
        if selected_index != 0 and selected_index <= len(recipe):
            # Get recipe
            name = recipe[selected_index - 1]["recipe_name"]
            description = recipe[selected_index - 1]["description"]
            ingredients = (recipe[selected_index - 1]["ingredients"])
            instructions = (recipe[selected_index - 1]["instructions"])

            # Special formatting
            ingredients = ingredients.replace(',', '\n -')
            instructions = instructions.replace('.', '.\n')

            # Format to table
            recipe_table = PrettyTable(align="l")
            recipe_table.field_names = [name]
            recipe_table.add_row([f'Description:\n{description}\n'])
            recipe_table.add_row([f'Ingredients:\n - {ingredients}\n'])
            recipe_table.add_row([f'Instructions:\n {instructions}'])
            result = recipe_table.get_string()  # Resulting recipe to display

    # Send response
    print("Responding with recipe...")
    time.sleep(1)
    socket.send_string(result)