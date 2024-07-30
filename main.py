import time
import json
import pyfiglet
from colorama import Fore
from prettytable import PrettyTable

# ---- PROMPTS ----
def welcome_prompt():
    print(pyfiglet.figlet_format("B i t e  B o o k", font="script").rstrip())
    print("Your own personal recipe catalog at the tips of your fingers!")

def catalog_header():
    print("\n-------------------------------------------------------")
    print("                    Recipe Catalog")
    print("-------------------------------------------------------")
    print("To view, search for, add, or delete a recipe in your")
    print("catalog, enter a selection and a short prompt will ask")
    print("you for additional details.\n")

def view_recipe_header():
    print("\n-------------------------------------------------------")
    print("                    View Recipe")
    print("-------------------------------------------------------")
    print("Enter in the index of the recipe you wish to view.")
    print("The recipe will be displayed and you can then choose")
    print("where you wish go next.")

def delete_header():
    print("\n-------------------------------------------------------")
    print("                   Delete Recipe")
    print("-------------------------------------------------------")
    print("To delete a recipe, please enter the index of the recipe.")
    print("After the action is completed, the updated catalog will be displayed.\n")


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

    catalog_header()
    time.sleep(1)

    # Receive response
    with open('view_catalog.txt', 'r') as file:
        display_recipe = file.read()
    print(display_recipe)

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
    print("\n-------------------------------------------------------")
    print("                   Add a Recipe")
    print("-------------------------------------------------------")
    print("To add a recipe, please fill out the following form.")
    print("To separate ingredients, utilize a comma.")
    print("To separate instructions, utilize a period.")
    print(Fore.RED + "After completing the form, you can choose to either\nsubmit the recipe, redo the recipe, or leave.\n" + Fore.RESET)

    # Input new recipe
    add_name = input("-- Enter recipe name: ")
    add_description = input("-- Enter description: ")
    add_ingredients = input("-- Enter ingredients: ")
    add_instructions = input("-- Enter instructions: ")
    new_item = {"recipe_name": add_name,
                "description": add_description,
                "ingredients": add_ingredients,
                "instructions": add_instructions}

    print("\n[ Do you wish to submit the recipe to the catalog? ]")
    print(f'YES: Submit recipe')
    print(f'REDO: Redo recipe')
    print(f'BACK: No, go bck to catalog\n')

    user_input = input("-- Enter your selection here: ").lower()
    if user_input == "yes":
        # Send request by writing new recipe to file
        with open('add.txt', 'w') as file:
            json.dump(new_item, file)
        print("\nPlease wait until the recipe has been added into the catalog...")
        time.sleep(2)
    elif user_input == "redo":
        add_recipe()
    elif user_input == "back":
        print("\nOk... Redirecting back to catalog.")
        time.sleep(1)
    view_catalog()




def search_recipe():    # IN PROGRESS --------
    print("\n-------------------------------------------------------")
    print("                   Search Recipe")
    print("-------------------------------------------------------")
    print("To search for a recipe, Enter in its' name.")
    print("If the recipe exists, the recipe will be displayed.")
    print("If it does not, you will be directed back to the catalog.\n")


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
    time.sleep(1)
    print(f'\nAre you sure you wish to delete the "{deleted_recipe}" recipe?')
    print(Fore.RED + "Please note that this action is permanent and cannot be undone.\n" + Fore.RESET)
    time.sleep(1)
    confirm = input("-- Enter 'YES' or enter 'NO': ").lower()
    if confirm == "yes":
        with open('catalog.txt', 'w+') as file:
            json.dump(new_catalog, file, indent=4)
    else:
        print("\nOk... Returning to catalog.")
        time.sleep(1)
    view_catalog()


# ---- OPTION PROMPTS ----
def main_options():
    print("\n-------------------------------------------------------")
    print("                        Home")
    print("-------------------------------------------------------")
    print("You can easily search or add to your catalog here.")
    print("To access additional features, view your catalog!")

    print("\n[ Home Options: ]")
    print("1: View catalog")
    print("2: Search for a recipe")
    print("3: Add recipe")
    print("QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ")
    if user_input == "1":       # view catalog
        view_catalog()
    elif user_input == "2":     # search
        search_recipe()
    elif user_input == "3":     # add
        add_recipe()
    elif user_input == "QUIT":  # exit
        exit_app()
    else:
        print("Invalid Input. Please make a valid choice.")

def catalog_options():
    print("\n[ Catalog Options: ]")
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
    print("Where would you like to go next?")
    print("BACK: Back to catalog")
    print("QUIT: Exit app\n")
    user_input = input("-- Enter your selection here: ").lower()

    if user_input == "back":
        view_catalog()

    elif user_input == "quit":
        exit_app()



if __name__ == "__main__":
    welcome_prompt()
    while True:
        main_options()