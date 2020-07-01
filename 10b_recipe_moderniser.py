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
    scale_factor = 0
    dodgy_sf = "yes"
    while dodgy_sf == "yes":

        serving_size = num_check("What is the recipe serving size? ")
        desired_size = num_check("How many servings are needed? ")

        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small "
                             "and you might struggle to accurately weigh"
                             "the ingredients. \n"
                             "Do you want to fix this and make more servings?").lower()
        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might"
                             "have issues with mixing bowl space / oven space. \n"
                             "Do you want to fix this and make a smaller batch? ").lower()

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

    return all_ingredients


def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]


def unit_checker():

    unit_to_check = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t", "teaspoon"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
    ounce = ["oz", "ounce", "fl oz", "ounces"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    mls = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
    litre = ["litre", "liter", "1", "litres", "liters"]
    pound = ["pound", "1b", "#", "pounds"]
    grams = ["g", "gram", "grams"]

    if unit_to_check == "":
    # print("you choose {}".format(unit_tocheck))
        return unit_to_check
    elif unit_to_check.lower() in grams:
        return "g"
    elif unit_to_check == "T" or unit_to_check.lower() in tablespoon:
        return "tbs"
    elif unit_to_check.lower() in teaspoon:
        return "tsp"
    elif unit_to_check.lower() in ounce:
        return "ounce"
    elif unit_to_check.lower() in cup:
        return "cup"
    elif unit_to_check.lower() in pint:
        return "pint"
    elif unit_to_check.lower() in quart:
        return "quart"
    elif unit_to_check.lower() in mls:
        return "ml"
    elif unit_to_check.lower() in litre:
        return "litre"
    elif unit_to_check.lower() in pound:
        return "pound"


# ****** Main Routine Goes here *******

# dictionaries go here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "ml": 1
}

# *** Generate food dictionary *****
# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

# print(food_dictionary)

# set up lists to hold original and 'modernised' recipes
modernised_recipe = []

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                    "The recipe name can't be blank and can't contain numbers",
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
mixed_regex= "\d{1,3}\s\d{1,3}\/\d{1,3}"
convert = "yes"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # Get amount...
    if re.match(mixed_regex, recipe_line):
        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)
        amount = amount * scale_factor

        # Get unit and ingredients...
        compile_regex = re.compile(mixed_regex)
        print(compile_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()  # remove extra white space

    else:
        get_amount = recipe_line.split(" ", 1)  # splits line at first space

        try:
            amount = eval(get_amount[0])    # convert amount to float if possible
            amount *= scale_factor

        # line has no amount (eg: pinch of salt)
        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)    # splits text at first space
    # print(get_unit)

    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        # GK Added, if unit in grams, add to list
        if unit == "g":
            modernised_recipe.append("{:.0f} g {}".format(amount, ingredient))
            continue

        # convert to mls if possible...
        amount = general_converter(amount, unit, unit_central, 1)
        print("Amount from ml converter", amount)

        # try convert to grams...
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

            # if the ingredient is in the list, convert it
            if amount_2[1] == "yes":
                modernised_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient))

            # if the ingredient is not in the list, leave the unit as ml
            else:
                modernised_recipe.append("{:.0f} ml {}".format(amount[0], ingredient))
                continue
        # Unit is not in mls, add scaled ingredient to list with unchanged unit
        else:
            modernised_recipe.append("{:.2f} {} {}".format(amount, unit_ingredient))
        continue

    # number of space is 1 (or less)!!
    else:
        # Item only has ingredient (no unit)
        modernised_recipe.append("{:.2f} {}".format(amount, unit_ingredient))

# Put updated ingredient in list

# Output ingredient list
for item in modernised_recipe:
    print(item)

