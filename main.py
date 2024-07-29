import time
import json
import pyfiglet
from colorama import Fore

# ---- PROMPTS ----
def welcome_prompt():
    print("-------------------------------------------------------")
    print(pyfiglet.figlet_format("B i t e  B o o k", font="script").rstrip())
    print("            Welcome to your recipe catalog!")
    print("-------------------------------------------------------")

def load_prompt(sec):
    print(Fore.BLUE + "\n Loading - Please wait!")
    for x in range(sec):
        time.sleep(1)
        print("          .")
    print(Fore.RESET)

# ---- ACTIONS ----

def exit_app():
    print("\n-------------------------------------------------------")
    print("                     Ok, goodbye!")
    print("-------------------------------------------------------\n")
    exit()

def view_catalog():
    # Send request by writing "Run" to file
    with open('view_catalog.txt', 'w') as file:
        file.write("Run")

    load_prompt(3)

    # Receive response
    with open('view_catalog.txt', 'r') as file:
        display_recipe = file.read()

    print(display_recipe)

    # Catalog has own set of options
    catalog_options()


def view_recipe():
    selected_index = input("-- Enter the index of the recipe you want to view: ")
    selected_index = selected_index

    # Send request by writing index to file
    with open('view_recipe.txt', 'w') as file:
        file.write(selected_index)

    # Receive response
    load_prompt(5)
    with open('view_recipe.txt', 'r') as file:
        display_recipe = file.read()

    print(display_recipe)

def add_recipe():
    print("\n-------------------------------------------------------")
    print("                   Add a Recipe")
    print("-------------------------------------------------------")
    print("To add a recipe, please fill out the following form.")
    print("To separate ingredients, utilize a comma.")
    print("To separate instructions, utilize a period.\n")

    # Input new recipe
    add_name = input("-- Enter recipe name: ")
    add_description = input("-- Enter description: ")
    add_ingredients = input("-- Enter ingredients: ")
    add_instructions = input("-- Enter instructions: ")
    new_item = {"recipe_name": add_name,
                "description": add_description,
                "ingredients": add_ingredients,
                "instructions": add_instructions}

    # Send request by writing new recipe to file
    with open('add.txt', 'w') as file:
        json.dump(new_item, file)

    print("\nPlease wait until the recipe has been added into the catalog...")
    load_prompt(4)

    print("Success!")

# ---- OPTION PROMPTS ----
def main_options():
    print("\nHomepage Options:")
    print("1: View recipe catalog")
    print("2: Add a recipe")
    print("3: I need help!")
    print("*: Exit app\n")

    user_input = input("-- Enter your selection here: ")
    if user_input == "1":  # view catalog
        view_catalog()
    elif user_input == "2":  # add recipe
        add_recipe()
    elif user_input == "3":  # help page
        pass
    elif user_input == "*":  # exit
        exit_app()
    else:
        print("Invalid Input. Please make a valid choice.")

def catalog_options():
    print("\nCatalog Options:")
    print("1: View recipe")
    print("2: Add recipe")
    print("3: Back to Homepage")
    print("*: Exit app\n")

    user_input_2 = input("-- Enter your selection here: ")

    if user_input_2 == "1":
        view_recipe()

    elif user_input_2 == "2":
        add_recipe()

    elif user_input_2 == "3":
        main_options()

    elif user_input_2 == "*":
        exit_app()

    else:
        print("\nInvalid selection...")
        time.sleep(1)
        print("Please enter a new selection.\n")
        time.sleep(1)
        catalog_options()

    #  ---- FOR FUTURE USE ----
    # print("3: Delete a recipe [not done]")
    # print("4: Edit a recipe [not done]")
    # print("5: Nothing - go back to home page\n")

    # elif user_input_2 == "3":
    #     pass
    #
    # elif user_input_2 == "4":
    #     main_options()

def back_option():
    print("Where would you like to go next?")
    print("1: Back to catalog")
    print("2: Back to home")
    print("3: Exit\n")
    user_input = input("-- Enter your selection here: ")

    if user_input == "1":
        view_catalog()

    elif user_input == "2":
        main_options()

    elif user_input == "3":
        exit_app()


if __name__ == "__main__":
    welcome_prompt()
    while True:
        main_options()