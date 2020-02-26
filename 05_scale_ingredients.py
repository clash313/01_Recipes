# Ingredients List


# Number Checking Function
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

# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit():
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
# Main Routine...

# Replace line below with component3 in due course...
scale_factor = float(input("Scale Factor: "))

# Set up empty ingredient list
ingredients = []

# Loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":

    amount = num_check("What is the amount for the ingredients? ")
    scaled = amount * scale_factor

    # Ask user for ingredient (via not blankfunction)
    get_ingredient = not_blank("Please type in an ingredient name: "
                               "This can't be blank",
                               "yes")

    # Stop looping if exit code is typed and there are more
    # than 2 ingredients...
    if get_ingredient.lower()=="xxx" and len(ingredients) > 1:
        break

    elif get_ingredient.lower() == "xxx" and len(ingredients) <2:
        print("you need at least two ingredients in teh list.  "
              "Please add more ingredients.")

    # If exit code is not entered,add ingredient to list
    else:
        ingredients.append(get_ingredient)




# Output list
print(ingredients)