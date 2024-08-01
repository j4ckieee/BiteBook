import zmq
import time
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4684")

while True:
    #  Wait for next request from client
    print("Waiting for request...")
    message = socket.recv_json()

    # Load existing catalog
    print("Loading catalog...")
    time.sleep(1)

    temp_list = []
    if os.path.exists('catalog.txt'):
        try:
            with open('catalog.txt', 'r') as file:
                raw_content = file.read()
                print(f"Raw file content:\n{raw_content}")  # Debugging line
                temp_list = json.loads(raw_content)
                if not isinstance(temp_list, list):
                    print("Error: Loaded data is not a list.")
                    temp_list = []
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            print("The content of the file is not valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("catalog.txt not found. Initializing with an empty list.")

    print(f"Loaded catalog: {temp_list}")

    # Add new recipe to catalog
    print("Adding recipe...")
    time.sleep(1)
    temp_list.append(message)

    with open('catalog.txt', 'w') as cat_file:
        json.dump(temp_list, cat_file, indent=4)

    # Clear add file
    print("Recipe added to catalog successfully!\n")

    print("Sending catalog...\n")
    time.sleep(1)

    socket.send_string("Done")