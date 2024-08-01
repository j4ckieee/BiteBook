import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4688")


while True:
    #  Wait for request from client
    print("Waiting for request...")
    del_index = socket.recv_string()

    # Received request
    del_index = int(del_index) - 1      # index offset by 1
    print(f"Received request to remove index {del_index}...")
    time.sleep(1)

    print(f"Deleting item from index...")

    new_catalog = []
    result = "Index does not exist in catalog."
    with (open('catalog.txt', 'r') as file):
        recipe_data = json.load(file)

        # Update catalog - Exclude data at selected del_index
        for idx, recipe in enumerate(recipe_data, 0):
            if idx != del_index:
                curr_recipe = recipe_data[idx]
                new_catalog.append(curr_recipe)
            else:
                result = "Item successfully deleted"    # del_index found
                continue

        # Update catalog with new version
        with open('catalog.txt', 'w+') as update_file:
            json.dump(new_catalog, update_file, indent=4)




    socket.send_string(result)


