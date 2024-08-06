import zmq
import time
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4684")

while True:
    #  Wait for request from client
    print("Waiting for request...")
    new_recipe = socket.recv_json()

    # Received request
    print(f'Received recipe named {new_recipe["recipe_name"]}')
    time.sleep(1)

    # Accessing catalog
    temp_list = []
    if os.path.exists('catalog.txt'):
        try:
            with open('catalog.txt', 'r') as file:
                all_recipes = file.read()
                temp_list = json.loads(all_recipes)
                if not isinstance(temp_list, list):
                    print("Recipes not stored as list.")
                    temp_list = []
        except:
            print(f"An unexpected error occurred")
    else:
        print("catalog.txt not found. Initializing with an empty list.")

    # Add new recipe to catalog
    print("Adding recipe...")
    time.sleep(1)
    temp_list.append(new_recipe)
    with open('catalog.txt', 'w') as cat_file:
        json.dump(temp_list, cat_file, indent=4)

    time.sleep(1)
    # Send response
    print("Recipe added to catalog successfully!\n")
    socket.send_string("Recipe was added successfully!")