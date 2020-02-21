# To do

# Ask user for servings made by recipe (and check this is a number that is more than that
# Ask user for servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than 00-25 or more than 4

# Function go here



# Main Routine goes here

serving_size = float(input("What is the recipe serving size? "))
desired_size = float(input("How many servings are needed? "))

scale_factor = desired_size / serving_size

print("Scale Factor: {}".format(scale_factor))