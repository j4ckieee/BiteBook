import time
import json
import os

def add_recipe():
    if os.path.exists('add.txt'):
        with open('add.txt', 'r') as add_file:
            try:
                new_recipe = json.load(add_file)
            except:
                return  # Return if nothing in file

        # Load existing catalog
        print("Loading catalog...")
        time.sleep(1)
        if os.path.exists('catalog.txt'):
            with open('catalog.txt', 'r') as cat_file:
                try:
                    temp_list = json.load(cat_file)
                except json.JSONDecodeError:
                    temp_list = []
        else:
            temp_list = []

        # Add new recipe to catalog
        print("Adding recipe...")
        time.sleep(1)
        temp_list.append(new_recipe)
        with open('catalog.txt', 'w') as cat_file:
            json.dump(temp_list, cat_file, indent=4)

        # Clear add file
        os.remove('add.txt')

        print("Recipe added to catalog successfully!\n")

while True:
    add_recipe()
    time.sleep(5)