# To do

# Ask user for servings made by recipe (and check this is a number that is more than that
# Ask user for servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than 00-25 or more than 4

# Function go here

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


# Main Routine goes here
sf_ok = "no"
while sf_ok == "no":

    serving_size = num_check("What is the recipe serving size? ")
    desired_size = num_check("How many servings are needed? ")

    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        sf_ok = input("Warning: This scale factor is very small and you "
                      "might struggle to accurately weigh the ingredients.  \n"
                      "Do you want to fix this and make more servings? ").lower()
    elif scale_factor > 4:
        sf_ok = input("Warning: This scale factor is quite large - you might"
                      "have issues with mixing bowl volumes and oven space.  "
                      "\nDo you want to keep going (type 'no' to change"
                      "your desired serving size ")


print("Scale Factor: {}".format(scale_factor))