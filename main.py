import time
import pyfiglet
from colorama import Fore
import zmq

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
    context.term()
    exit()

def view_catalog():
    # Connecting to view catalog server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4680")

    # Send "Run
    socket.send_string("Run")

    load_prompt(3)

    #  Get the reply
    message = socket.recv()
    print(message.decode()+ "\n")

    # Catalog has own set of options
    catalog_options()

def view_recipe(selected_index):
    # Connecting to view catalog server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4682")

    socket.send_json(selected_index)
    load_prompt(3)

    #  Get the reply
    message = socket.recv()
    print(message.decode())

def add_recipe():
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4684")

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
        # Connecting to view catalog server
        new_item = new_item

        # Send "Run
        socket.send_json(new_item)

        #  Get the reply
        message = socket.recv()
        print(message.decode())
    elif user_input == "NO":
        print("\nOk... Redirecting back to catalog.")
        time.sleep(1)
    elif user_input == "REDO":
        add_recipe()

    view_catalog()



def search_recipe():
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4686")

    search_header()

    user_input = str(input("-- Enter recipe name: ")).lower()

    socket.send_string(user_input)
    message = socket.recv_string()
    print(message)
    back_option()


def delete_recipe():    # IN PROGRESS --------
    delete_header()

    # Connecting to view catalog server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4688")
    num_sel = input("-- Enter the index of the recipe you want to delete: ")

    print(f'\nAre you sure you want to delete this recipe?')
    print(Fore.RED + "Please note that this action is permanent and cannot be undone.\n" + Fore.RESET)

    print("[ Delete Options: ]")
    print("YES: Delete recipe")
    print("NO: Do NOT delete recipe\n")

    confirm = input("-- Enter your selection here: ").upper()
    if confirm == "YES":
        socket.send_string(num_sel)

        #  Get the reply
        delete_selection = socket.recv_string()
        print("\n" + delete_selection)
    elif confirm == "NO":
        print("\nRecipe not deleted.")
    else:
        print("Invalid input.\n")
    time.sleep(1)
    print("Redirecting back to catalog.")
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
        selected_index = input("-- Enter the index of the recipe you want to view: ")
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
    context = zmq.Context()
    app_logo()
    while True:
        main_options()