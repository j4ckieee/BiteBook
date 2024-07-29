import time
import json

while True:
    add_file = open("add.txt", "w+")
    try:
        new_recipe = json.load(add_file)
    except:
        continue

    if new_recipe:
        print("\nPreparing catalog...")
        with open('catalog.txt', 'r') as cat_file:
            try:
                temp_list = json.load(cat_file)
            except:
                temp_list = []

        print("Adding recipe into catalog...")
        time.sleep(1)
        with open('catalog.txt', 'w') as file:
            temp_list.append(new_recipe)
            json.dump(temp_list, file, indent=4)
        print("Success!")

    add_file.close()