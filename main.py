import time
import os
import json
import pyfiglet
from prettytable import PrettyTable
from colorama import Fore

# ---- PROMPTS ----
def welcome_prompt():
    print("-------------------------------------------------------")
    print(pyfiglet.figlet_format("B i t e  B o o k", font="script").rstrip())
    print("            Welcome to your recipe catalog!")
    print("-------------------------------------------------------")

def load_prompt(wait_time):
    print(Fore.BLUE + "\n Loading - Please wait!")
    for x in range(wait_time):
        time.sleep(0.5)
        print("          .")
    print(Fore.RESET)

# ---- ACTIONS ----

def exit_app():
    print("\n----------------------------------------------------------------")
    print("                       Ok, goodbye!")
    print("----------------------------------------------------------------\n")
    exit()

def view_catalog():
    if os.path.exists("catalog.txt"):
        try:
            with open('catalog.txt', 'r') as file:
                catalog_table = PrettyTable()
                catalog_table.field_names = ["", "Recipe Name", "Description"]
                recipe_data = json.load(file)
                for count, recipe in enumerate(recipe_data, start=1):
                    catalog_table.add_row([count, recipe["recipe_name"], recipe["description"]])
                print(catalog_table)
                time.sleep(1)
                catalog_options()
        except:
            print("\nWait - there is nothing in your catalog!")
            time.sleep(1)
            print("Please add a recipe before proceeding.")
            time.sleep(2)
    else:
        print("\nWait - there is nothing in your catalog!")
        time.sleep(1)
        print("Please add a recipe before proceeding.")
        time.sleep(2)


def view_recipe():
    selected_index = input("-- Enter the index of the recipe you want to view: ")
    selected_index = int(selected_index)

    load_prompt(3)

    with open('catalog.txt', 'r') as file:
        recipe = json.load(file)
        if selected_index != 0 and selected_index <= len(recipe):
            name = recipe[selected_index - 1]["recipe_name"]
            description = recipe[selected_index - 1]["description"]
            ingredients = (recipe[selected_index - 1]["ingredients"])
            instructions = (recipe[selected_index - 1]["instructions"])

            # special formatting
            ingredients = ingredients.replace(',', '\n -')
            instructions = instructions.replace('.', '.\n')

            # display recipe
            recipe_table = PrettyTable(align="l")
            recipe_table.field_names = [name]
            #recipe_table.add_row([f'Recipe Name:\n{name}\n'])
            recipe_table.add_row([f'Description:\n{description}\n'])
            recipe_table.add_row([f'Ingredients:\n - {ingredients}\n'])
            recipe_table.add_row([f'Instructions:\n {instructions}'])

            print(recipe_table, "\n")
            time.sleep(1)
            back_option()
        else:
            print("\nInvalid selection...")
            time.sleep(1)
            print("Redirecting back to catalog...\n")
            time.sleep(1)
            view_catalog()

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

    # Add to catalog
    with open('add.txt', 'w') as file:
        json.dump(new_item, file)

    time.sleep(1)
    print("\nPlease wait until the recipe has been added into the catalog...")
    load_prompt(4)

    print("Success!")

# ---- OPTION PROMPTS ----
def main_options():
    print("\nHomepage Options:")
    print("1: View recipe catalog")
    print("2: Add a recipe")
    print("3: Delete a recipe [not done] ")
    print("4: Search for a recipe [not done]")
    print("5: I need help!")
    print("6: Exit\n")

    user_input = input("-- Enter your selection here: ")
    if user_input == "1":  # view catalog
        load_prompt(3)
        view_catalog()
    elif user_input == "2":  # add recipe
        add_recipe()
    elif user_input == "3":  # delete recipe
        pass
    elif user_input == "4":  # search recipe
        pass
    elif user_input == "5":  # help page
        pass
    elif user_input == "6":  # exit
        exit_app()
    else:
        print("Invalid Input. Please make a valid choice.")

def catalog_options():
    print("\nCatalog Options:")
    print("1: View recipe")
    print("2: Add recipe")
    print("3: Back to Homepage")

    user_input_2 = input("\n-- Enter your selection here: ")

    if user_input_2 == "1":
        view_recipe()

    elif user_input_2 == "2":
        add_recipe()

    elif user_input_2 == "3":
        main_options()
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
        load_prompt(3)
        view_catalog()

    elif user_input == "2":
        main_options()
    elif user_input == "3":
        exit_app()


if __name__ == "__main__":
    welcome_prompt()
    while True:
        main_options()
