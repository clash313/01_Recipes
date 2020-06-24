# modules to be used...
import csv
import re

# ***** Functions ******

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Number checking function (number must be a float that is more than 0)
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def get_sf():
    serving_size = num_check("What is the recipe serving size? ")

    # Main Routine goes here
    dodgy_sf = "yes"
    while dodgy_sf == "yes":

        desired_size = num_check("How many servings are needed? ")

        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small and you "
                             "might struggle to accurately weigh the ingredients.  \n"
                             "Do you want to fix this and make more servings? ").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might"
                             "have issues with mixing bowl volumes and oven space.  "
                             "\nDo you want to fix this and make a smaller"
                             "batch? ").lower()
        else:
            dodgy_sf = "no"

    return scale_factor


 # Function to get (and check amount, unit and ingredient)
def get_all_ingredients():
    all_ingredients = []

    stop = ""
    print("Please enter ingredients one line at a time.  Press 'xxx' to when "
          "you are done.")
    if __name__ == '__main__':
        while stop != "xxx":
            # Ask user for ingredient (via not blank function)
            get_recipe_line = not_blank("Recipe Line: ",
                                        "This can't be blank",
                                        "yes")

            # Stop loopin if exit code is typed and there are more
            # than 2 ingredients..
            if get_recipe_line.lower() == "xxx" and len(all_ingredients) > 1:
                break

            elif get_recipe_line.lower() == "xxx" and len(all_ingredients) <2:
                print("You need at least two ingredients in the list.  "
                      "Please add more ingredients.")

            # If exit code is not entered, add ingredient to list
            else:
                all_ingredients.append(get_recipe_line)


# ***** Main Routine ******

# set up Dictionaries

# set up list to hold 'modernised' ingredients

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank and can't contain numbers, ",
                        "no")
# Ask user where the recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank",
                   "yes")


# Get serving sizes and scale factor
scale_factor = get_sf()

# Get amounts, units and ingredient from user...
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient...



# Convert unit to ml
# Convert from ml to g
# Put updated ingredient in list

# Output ingredient list

