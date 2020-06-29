# Conversion Function...

import csv

# ***** Functions go here ******
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor


    else:
        converted = "no"

    return how_much

def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "ounce", "fl oz"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    mls = ["ml", "milliliter", "millilitre"]
    litre = ["litre", "litre", "1"]
    pound = ["pound", "1b", "#"]

    if unit_tocheck == "":
    # print("you choose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "ml"
    elif unit_tocheck.lower() in litre:
        return "litre"
    elif unit_tocheck.lower() in pound:
        return "pound"

# ****** Main Routine Goes here *******

# dictionaries go here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup" : 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000
    "ml": 1
}

# *** Generate food dictionary *****
# open file
groceries = open('01_ingredients_ml_to_g.csv')
