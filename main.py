import time
import pyfiglet
from colorama import Fore
import zmq

# ------ PAGES ------
def app_logo():
    print(pyfiglet.figlet_format("  B i t e  B o o k", font="script").rstrip())
    print("Your own personal recipe catalog at the tips of your fingers!")

def home_page():
    instructions = ("You can easily view, search, or add to your catalog here.\n"
                    "To access additional features, proceed to your catalog!\n")
    display_header("Home", 32, instructions)

    home_options()

def catalog_page():
    instructions = ("You can easily view, search, or add to your catalog here.\n"
                    "To access additional features, proceed to your catalog!\n")
    display_header("Recipe Catalog", 38, instructions)

    view_catalog()
    catalog_options()

def recipe_page():
    instructions = ("Enter in the index of the recipe you wish to view. The recipe\n"
                    "will be displayed and you can then choose where you wish go next.\n")
    display_header("View Recipe", 30, instructions)

    selected_index = input("-- Enter the index of the recipe you want to view: ")
    view_recipe(selected_index)
    back_option()

def add_page():
    instructions = ("To add a recipe, please fill out the following form.\n"
                    "To separate ingredients, utilize a comma.\n"
                    "To separate instructions, utilize a period.\n")
    display_header("Add a Recipe", 37, instructions)
    print(Fore.RED + "After completing the form, you can choose to submit the recipe, \n"
                     "redo the recipe, or go back to the catalog.\n" + Fore.RESET)

    # Get user input for new recipe
    add_name = input("-- Enter recipe name: ")
    add_description = input("-- Enter description: ")
    add_ingredients = input("-- Enter ingredients: ")
    add_instructions = input("-- Enter instructions: ")
    new_item = {"recipe_name": add_name,
                "description": add_description,
                "ingredients": add_ingredients,
                "instructions": add_instructions}

    # Confirm recipe submission
    print("\n[ Do you wish to submit this recipe to the catalog? ]")
    print(f'YES: Submit recipe')
    print(f'NO: Cancel and go back to catalog')
    print(f'REDO: Redo recipe\n')

    user_input = input("-- Enter your selection here: ").upper()
    if user_input == "YES":
        add_recipe(new_item)
    elif user_input == "NO":
        print("\nOk... Redirecting back to catalog.")
        time.sleep(1)
    elif user_input == "REDO":
        add_page()

    catalog_page()

def search_page():
    instructions = ("To search for a recipe, enter in the recipes' name.\n"
                    "If the recipe exists, the recipe will be displayed.\n"
                    "If it does not, you can choose where you would like to\nproceed next.\n")
    display_header("Search Recipe", 37, instructions)

    find_recipe = str(input("-- Enter recipe name: ")).lower()
    search_recipe(find_recipe)
    back_option()

def delete_page():
    instructions = ("To delete a recipe, please enter the index of the recipe. After\n"
                    "the action is completed, the updated catalog will be displayed.\n")
    display_header("Delete Recipe", 37, instructions)

    delete_index = input("-- Enter the index of the recipe you want to delete: ")

    print(f'\nAre you sure you want to delete this recipe?')
    print(Fore.RED + "Please note that this action is permanent and cannot be undone.\n" + Fore.RESET)

    print("[ Delete Options: ]\n"
          "YES: Delete recipe\n"
          "NO: Do NOT delete recipe\n")

    confirm = input("-- Enter your selection here: ").upper()
    if confirm == "YES":
        delete_recipe(delete_index)
    elif confirm == "NO":
        print("\nRecipe not deleted.")
    else:
        print("Invalid input.\n")

    time.sleep(1)
    print("Redirecting back to catalog.")
    time.sleep(1)
    catalog_page()

def convert_page():
    instructions = ("Enter in the amount and unit of what you want to convert from,\n"
                    "and what unit you want to convert to.\n")
    display_header("Unit Conversion Tool", 40, instructions)

    print(Fore.RED + "This tool only works for the following units:\n"
                     "oz, lb, tsp, tbsp, fl oz, cup, pt, qt, gal\n" + Fore.RESET)

    print("[ Input what you're converting \033[1mFROM...\033[0m ]")
    amount_input = input("-- Enter numeric amount: ")
    unit_from_input = input("-- Enter unit: ")

    print("\n[ Input what you're converting \033[1mTO...\033[0m ]")
    unit_to_input = input("-- Enter unit: ")

    unit_from_input = unit_from_input.lower()
    unit_to_input = unit_to_input.lower()
    convert_data = {"amount": amount_input,
                    "unit_from": unit_from_input,
                    "unit_to": unit_to_input}

    convert_unit(convert_data)
    back_option()

def exit_page():
    display_header("G o o d b y e !", 40, "")
    context.term()
    exit()

# ------ OPTIONS ------
def home_options():
    print("[ Home Options: ]\n"
          "1: View catalog\n"
          "2: Search for a recipe\n"
          "3: Add recipe\n"
          "CONVERT: Unit conversion tool\n"
          "QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ")

    if user_input.isalpha():
        user_input = user_input.upper()

    while user_input != "QUIT":
        if user_input == "1":
            catalog_page()
        elif user_input == "2":
            search_page()
        elif user_input == "3":
            add_page()
        elif user_input == "CONVERT":
            convert_page()
        else:
            user_input = input("-- Invalid input - enter your selection here: ")
    exit_page()

def catalog_options():
    print("[ Catalog Options: ]\n"
          "1: View a recipe\n"
          "2: Search for a recipe\n"
          "3: Add recipe\n"
          "4: Delete recipe\n"
          "CONVERT: Unit conversion tool\n"
          "BACK: Back to homepage\n"
          "QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ")

    if user_input.isalpha():
        user_input = user_input.upper()

    if user_input == "1":
        recipe_page()

    elif user_input == "2":
        search_page()

    elif user_input == "3":
        add_page()

    elif user_input == "4":
        delete_page()

    elif user_input == "CONVERT":
        convert_page()

    elif user_input == "BACK":
        home_page()

    elif user_input == "QUIT":
        exit_page()

    else:
        print("\nInvalid selection...")
        time.sleep(1)
        print("Please enter a new selection.\n")
        time.sleep(1)
        catalog_options()

def back_option():
    print("[ Where would you like to go next? ]\n"
          "CONVERT: Unit Conversion Tool\n"
          "BACK: Back to catalog\n"
          "QUIT: Exit app\n")

    user_input = input("-- Enter your selection here: ").upper()

    if user_input == "CONVERT":
        convert_page()

    elif user_input == "BACK":
        catalog_page()

    elif user_input == "QUIT":
        exit_page()


# ------ MISC PROMPTS ------
def display_header(page_name, spacing, instructions):
    divider = "--------------------------------------------------------------"
    padded_text = page_name.rjust(spacing)
    print(divider)
    print(padded_text)
    print(divider)
    print(instructions)

# def load_prompt(sec):
#     print(Fore.GREEN + "\n                    Loading - Please wait!")
#     for x in range(sec):
#         time.sleep(1)
#         print("                              .")
#     print(Fore.RESET)

# ------ MICROSERVICES ------
def view_catalog():
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4680")

    socket.send_string("Run")

    message = socket.recv()
    print(message.decode()+ "\n")

def view_recipe(selected_index):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4682")

    socket.send_json(selected_index)

    # # Let server do work
    # load_prompt(2)

    message = socket.recv()
    print(message.decode())

def add_recipe(new_item):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:8648")

    socket.send_json(new_item)

    message = socket.recv()
    print(message.decode())

def search_recipe(find_recipe):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7645")

    socket.send_string(find_recipe)
    message = socket.recv_string()
    print(message)

def delete_recipe(delete_index):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4694")

    socket.send_string(delete_index)

    delete_selection = socket.recv_string()
    print("\n" + delete_selection)


def convert_unit(convert_data):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4600")

    socket.send_json(convert_data)

    time.sleep(1)

    convert_result = socket.recv_string()
    print(f'\n\033[1mResult:\033[0m {convert_result}\n' )

if __name__ == "__main__":
    context = zmq.Context()
    app_logo()
    while True:
        home_page()