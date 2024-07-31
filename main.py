import time
import json
import pyfiglet
from colorama import Fore
from prettytable import PrettyTable

# ---- PROMPTS ----
def app_logo():
    print(pyfiglet.figlet_format("  B i t e  B o o k", font="script").rstrip())
    print("Your own personal recipe catalog at the tips of your fingers!")

def home_header():
    print("--------------------------------------------------------------")
    print("                           Home")
    print("--------------------------------------------------------------")
    print("You can easily view, search, or add to your catalog here.")
    print("To access additional features, proceed to your catalog!\n")

def catalog_header():
    print("--------------------------------------------------------------")
    print("                      Recipe Catalog")
    print("--------------------------------------------------------------")
    print("To view, search for, add, or delete a recipe in your catalog,")
    print("make a selection and you will be redirected to a short form.\n")

def view_recipe_header():
    print("\n--------------------------------------------------------------")
    print("                    View Recipe")
    print("--------------------------------------------------------------")
    print("Enter in the index of the recipe you wish to view.")
    print("The recipe will be displayed and you can then choose")
    print("where you wish go next.\n")

def search_header():
    print("\n--------------------------------------------------------------")
    print("                   Search Recipe")
    print("--------------------------------------------------------------")
    print("To search for a recipe, enter in the recipes' name.")
    print("If the recipe exists, the recipe will be displayed.")
    print("If it does not, you can choose where you would like to\nproceed next.\n")


def add_header():
    print("\n--------------------------------------------------------------")
    print("                       Add a Recipe")
    print("--------------------------------------------------------------")
    print("To add a recipe, please fill out the following form.")
    print("To separate ingredients, utilize a comma.")
    print("To separate instructions, utilize a period.")
    print(Fore.RED + "After completing the form, you can choose to submit the recipe, \nredo the recipe, or go back to the catalog.\n" + Fore.RESET)

def delete_header():
    print("\n--------------------------------------------------------------")
    print("                       Delete Recipe")
    print("--------------------------------------------------------------")
    print("To delete a recipe, please enter the index of the recipe.")
    print("After the action is completed, the updated catalog will be displayed.\n")


def load_prompt(sec):
    print(Fore.GREEN + "\n                    Loading - Please wait!")
    for x in range(sec):
        time.sleep(1)
        print("                              .")
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

    # Allow microservice to work
    load_prompt(4)  # [WARNING... BE CAREFUL WHEN CHANGING!] - Originally just 3

    catalog_header()

    # Receive response
    with open('view_catalog.txt', 'r') as file:
        display_catalog = file.read()
        while display_catalog == "Run":
            display_catalog = file.read()
    print(display_catalog +"\n")

    # Catalog has own set of options
    catalog_options()

def view_recipe(selected_index):
    # Send request by writing index to file
    with open('view_recipe.txt', 'w') as file:
        file.write(selected_index)

    # Receive response
    load_prompt(4)
    with open('view_recipe.txt', 'r') as file:
        display_recipe = file.read()

    print(display_recipe)

def add_recipe():
    add_header()

    # Input new recipe
    add_name = input("-- Enter recipe name: ")
    add_description = input("-- Enter description: ")
    add_ingredients = input("-- Enter ingredients: ")
    add_instructions = input("-- Enter instructions: ")
    new_item = {"recipe_name": add_name,
                "description": add_description,
                "ingredients": add_ingredients,
                "instructions": add_instructions}

    print("\n[ Do you wish to submit this recipe to the catalog? ]")
    print(f'YES: Submit recipe')
    print(f'NO: Cancel and go back to catalog')
    print(f'REDO: Redo recipe\n')

    user_input = input("-- Enter your selection here: ").upper()
    if user_input == "YES":
        # Send request by writing new recipe to file
        with open('add.txt', 'w') as file:
            json.dump(new_item, file)
        print("\nSubmitting recipe...")
        time.sleep(1)
        print("Success! Redirecting back to catalog.")
        time.sleep(1)
        # time.sleep(2)
    elif user_input == "NO":
        print("\nOk... Redirecting back to catalog.")
        time.sleep(1)
    elif user_input == "REDO":
        add_recipe()
    view_catalog()




def search_recipe():    # IN PROGRESS --------
    search_header()
    user_input = str(input("-- Enter recipe name: ")).lower()
    with open('catalog.txt', 'r') as file:
        all_recipes = json.load(file)
        for idx, recipe in enumerate(all_recipes, 1):
            curr_recipe = all_recipes[idx-1]["recipe_name"]
            curr_recipe = str(curr_recipe).lower()

            # Recipe found
            if curr_recipe == user_input:
                matching_index = str(idx)
                view_recipe(matching_index)
                return

        # Recipe NOT found
        load_prompt(1)
        print("Sorry - no matching recipe was found.")
        time.sleep(1)


def delete_recipe():    # IN PROGRESS --------
    delete_header()

    user_input = int(input("-- Enter index of the recipe you want to delete: ")) - 1
    new_catalog=[]
    with open('catalog.txt', 'r') as file:
        all_recipes = json.load(file)
        for idx, recipe in enumerate(all_recipes, 0):
            curr_recipe = all_recipes[idx]["recipe_name"]
            curr_recipe = str(curr_recipe).lower()

            # Populate new catalog
            if idx != user_input:
                curr_recipe = all_recipes[idx]
                new_catalog.append(curr_recipe)
            else:
                deleted_recipe = all_recipes[idx]["recipe_name"]
                continue

    print(f'\nAre you sure you wish to delete the "{deleted_recipe}" recipe?')
    print(Fore.RED + "Please note that this action is permanent and cannot be undone.\n" + Fore.RESET)

    print("[ Delete Options: ]")
    print("YES: Delete recipe")
    print("NO: Do NOT delete recipe\n")

    confirm = input("-- Enter your selection here: ").lower()
    if confirm == "yes":
        with open('catalog.txt', 'w+') as file:
            json.dump(new_catalog, file, indent=4)

        print("\nRecipe deleted...")
        time.sleep(1)
        print("Redirecting back to catalog.")
    else:
        print("\nOk... Returning to catalog.")
        time.sleep(1)
    view_catalog()


# ---- OPTION PROMPTS ----
def main_options():
    home_header()
    print("[ Home Options: ]")
    print("1: View catalog")
    print("2: Search for a recipe")
    print("3: Add recipe")
    print("QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ")

    while user_input != "QUIT" and user_input != "quit":
        if user_input == "1":       # view catalog
            view_catalog()
        elif user_input == "2":     # search
            search_recipe()
        elif user_input == "3":     # add
            add_recipe()
        else:
            user_input = input("-- Invalid input - enter your selection here: ")

    exit_app()


def catalog_options():
    print("[ Catalog Options: ]")
    print("1: View a recipe")
    print("2: Search for a recipe")
    print("3: Add recipe")
    print("4: Delete recipe")
    print("BACK: Back to homepage")
    print("QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ")

    if user_input == "1":
        view_recipe_header()
        selected_index = input("\n-- Enter the index of the recipe you want to view: ")
        view_recipe(selected_index)
        back_option()

    elif user_input == "2":
        search_recipe()
        back_option()

    elif user_input == "3":
        add_recipe()

    elif user_input == "4":
        delete_recipe()

    elif user_input == "BACK":
        main_options()

    elif user_input == "QUIT":
        exit_app()

    else:
        print("\nInvalid selection...")
        time.sleep(1)
        print("Please enter a new selection.\n")
        time.sleep(1)
        catalog_options()

def back_option():
    print("[ Where would you like to go next? ]")
    print("BACK: Back to catalog")
    print("QUIT: Exit app\n")
    user_input = input("-- Enter your selection here: ").lower()

    if user_input == "back":
        view_catalog()

    elif user_input == "quit":
        exit_app()

if __name__ == "__main__":
    app_logo()
    while True:
        main_options()