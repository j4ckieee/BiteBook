import zmq
import time
import json
from prettytable import PrettyTable

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4680")

while True:
    #  Wait for next request from client
    print("Waiting for request...")
    message = socket.recv()

    print("Receiving catalog...")
    time.sleep(1)
    with open('catalog.txt', 'r') as file:
        recipe_data = json.load(file)
        catalog_table = PrettyTable()
        catalog_table.field_names = ["", "Recipe Name", "Description"]
        for count, recipe in enumerate(recipe_data, start=1):
            catalog_table.add_row([count, recipe["recipe_name"], recipe["description"]])
        print("Catalog accessed...")
        time.sleep(1)
        result = catalog_table.get_formatted_string()

    print("Sending catalog...\n")
    time.sleep(1)

    socket.send_string(result)