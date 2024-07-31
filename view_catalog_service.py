import time
import json
from prettytable import PrettyTable

while True:
    with open('view_catalog.txt', 'r') as idx_file:
        txt = idx_file.read()

    if txt == "Run":
        print("'Run' received...")
        with open('catalog.txt', 'r') as file:
            catalog_table = PrettyTable()
            catalog_table.field_names = ["", "Recipe Name", "Description"]
            recipe_data = json.load(file)
            for count, recipe in enumerate(recipe_data, start=1):
                catalog_table.add_row([count, recipe["recipe_name"], recipe["description"]])
            print("Catalog accessed...")
        time.sleep(1)
        with open('view_catalog.txt', 'w') as file:
            file.write(catalog_table.get_string())
            print("Catalog submitted...")

        # except:
        #     print("Catalog NOT accessed...")
        #     with open('view_catalog.txt', 'w') as file:
        #         file.write("\nWait - there is nothing in your catalog!\nPlease add a recipe before proceeding.")