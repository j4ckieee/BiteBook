import time
import os
import json
import pyfiglet
from prettytable import PrettyTable

print(pyfiglet.figlet_format("B i t e  B o o k", font="script").rstrip())

print("-------------------------------------------------------")
print("        Hello, welcome to your recipe catalog!")
print("-------------------------------------------------------")

while True:
    print("\nOptions:")
    print("1: View all recipes")
    print("2: Add a new recipe")
    print("3: Delete a recipe [not implemented yet] ")
    print("4: Search for a recipe [not implemented yet]")
    print("5: Help")
    print("6: Exit \n")

    user_input = input("-- What would you like to do?: ")

    # view catalog
    if user_input == "1":
        if os.path.exists("catalog.txt"):
            try:
                with open('catalog.txt', 'r') as file:
                    print("\n-------------------------------------------------------")
                    print("                 View Recipe Catalog")
                    print("-------------------------------------------------------")
                    catalog_table = PrettyTable()
                    catalog_table.field_names = ["", "Recipe Name"]
                    recipe_data = json.load(file)
                    for count, recipe in enumerate(recipe_data, start=1):
                        catalog_table.add_row([count, recipe["recipe_name"]])
                    print(catalog_table)
            except:
                print("Sorry, nothing in catalog. Please add a new recipe before proceeding.\n")
        else:
            print("Sorry, nothing in catalog. Please add a new recipe before proceeding.\n")


    # add recipe
    elif user_input == "2":
        print("\n---------------")
        print("Add Recipe:")
        print("---------------")
        print("To add a recipe, please out the following form:")

        # Input new recipe
        add_name = input("-- Enter recipe name: ")
        add_description = input("-- Enter description: ")
        add_ingredients = input("-- Enter ingredients: ")
        new_item = {"recipe_name": add_name,
                    "description": add_description,
                    "ingredients": add_ingredients}

        # Add to catalog
        with open('add.txt', 'w') as file:
            json.dump(new_item, file)

        time.sleep(1)
        print("\nPlease wait until the recipe has been added into the catalog...")
        for x in range(3):
            time.sleep(1)
            print(".")

        print("Success!")

    # delete recipe
    elif user_input == "3":
        pass

    # search recipe
    elif user_input == "4":
        pass

    # exit
    elif user_input == "5":
        print("\n----------------------------------------------------------------")
        print("                       Ok, goodbye!")
        print("----------------------------------------------------------------\n")
        break
    else:
        print("Invalid Input. Please make a valid choice.")