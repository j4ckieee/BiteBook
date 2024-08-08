import zmq
import time
import json
from prettytable import PrettyTable

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4680")

while True:
    #  Wait for request from client
    print("Waiting for request...")
    message = socket.recv()

    # Received request
    print(f'Received request: {message.decode()}')
    #time.sleep(1)

    # Open catalog and add elements to table
    with open('catalog.txt', 'r') as file:
        recipe_data = json.load(file)
        catalog_table = PrettyTable()
        catalog_table.field_names = ["", "Recipe Name", "Description"]
        for count, recipe in enumerate(recipe_data, start=1):
            catalog_table.add_row([count, recipe["recipe_name"], recipe["description"]])
        print("Catalog accessed...")
        #time.sleep(1)
        result = catalog_table.get_formatted_string()   # Resulting table to display

    # Send response
    print("Sending response...\n")
    #time.sleep(1)
    socket.send_string(result)