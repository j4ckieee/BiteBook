import time
import os
import json
from prettytable import PrettyTable


print("\n----------------------------------------------------------------")
print("         Hello, welcome to your recipe catalog!")
print("----------------------------------------------------------------")

while True:
    print("\nSelect an Option:")
    print("1: View all recipes")
    print("2: Add a new recipe")
    print("3: Delete a recipe")
    print("4: Search for a recipe")
    print("5: Exit \n")

    user_input = input("-- What would you like to do?: ")

    # view catalog
    if user_input == "1":
        if os.path.exists("catalog.txt"):
            try:
                with open('catalog.txt', 'r') as file:
                    print("\n---------------")
                    print("Recipe Catalog")
                    print("\n---------------")
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
        add_description = input("-- Enter desc: ")
        new_item = {"recipe_name": add_name,
                    "description": add_description}

        # Add to catalog
        with open('add.txt', 'w') as file:
            json.dump(new_item, file)

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



