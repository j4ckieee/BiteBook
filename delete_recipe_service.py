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
    del_index = int(del_index) - 1      # Index offset by 1
    print(f"Received request to remove index {del_index}...")
    time.sleep(1)

    # Copy valid elements to new catalog
    print(f"Deleting item from index...")
    new_catalog = []
    result = "Index does not exist in catalog."
    with (open('catalog.txt', 'r') as file):
        recipe_data = json.load(file)
        for idx, recipe in enumerate(recipe_data, 0):
            if idx != del_index:    # Add item to new catalog
                curr_recipe = recipe_data[idx]
                new_catalog.append(curr_recipe)
            else:   # del_index found - exclude from new catalog
                result = "Item successfully deleted"
                continue

        # Replace catalog with new version
        with open('catalog.txt', 'w+') as update_file:
            json.dump(new_catalog, update_file, indent=4)

        print(f'Catalog updated...')
    # Send back result
    print(f'Responding with: {result}\n')
    socket.send_string(result)



