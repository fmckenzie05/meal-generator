# random_meal_gen.py

# List of ingredients that can be used in the meals
# Identify the requirements for the app. You will need to decide what types of meals you want to generate (breakfast, lunch, dinner, snacks, etc.), and what types of ingredients you want to include in the meals. You may also want to consider any dietary restrictions or preferences that you want to take into account.
# Create a list of ingredients that can be used in the meals. This list should include a variety of ingredients that are allowed on the keto diet, such as meats, fish, eggs, nuts, seeds, and low-carb vegetables.
# Write a function that generates a random meal from the list of ingredients. This function should take into account the types of meals you want to generate, as well as any dietary restrictions or preferences. You may want to use a random number generator to randomly select ingredients from the list to create the meal.
# Test the function to ensure that it is generating meals correctly. You may want to test the function with different inputs to ensure that it is working correctly and generating a variety of different meals.
# Integrate the function into a user interface. This can be a command-line interface, a web-based interface, or a mobile app, depending on your preferences and the needs of your users. The interface should allow users to specify their meal preferences and any dietary restrictions, and should display the generated meal to the user.
# Test the app with a small group of users to get feedback and make any necessary improvements.
# Implement restriction base on diet e.g lactose or type 2 diabetic.

import random
import pandas as pd

with open("./ingredients.csv", "w", "UTF-8") as ingredients:
    df_i = pd.read_csv(ingredients.csv)


# Function to generate a random meal from the list of ingredients
def generate_meal(meal_type):
    if meal_type == "breakfast":
        # Generate a random breakfast meal
        meal = random.sample(ingredients, 3)
        return "Breakfast: " + ", ".join(meal)
    elif meal_type == "lunch":
        # Generate a random lunch meal
        meal = random.sample(ingredients, 4)
        return "Lunch: " + ", ".join(meal)
    elif meal_type == "dinner":
        # Generate a random dinner meal
        meal = random.sample(ingredients, 5)
        return "Dinner: " + ", ".join(meal)
    elif meal_type == "snack":
        # Generate a random snack meals
        meal = random.sample(ingredients, 2)
        return "snack: " + ", ".join(meal)
    else:
        return "Invalid meal type"

def generate_drink(drink_type):
    if drink_type == "tea":
        # Generate a random tea drink
        drink = random.sample(tea, 1)
        return "tea: " + ", ".join(drink)
    if drink_type == "beer":
        # Generate a random beer drink
        drink = random.sample(beer, 1)
        return "beer: " + ", ".join(drink)

    else:
        return "water"

# Generate a random breakfast, lunch, and dinner
breakfast = generate_meal("breakfast")
lunch = generate_meal("lunch")
dinner = generate_meal("dinner")
snack = generate_meal("snack")

# Generate a random drink, tea, beer, and water
tea = generate_drink("tea")
beer = generate_drink("beer")

print(breakfast)
print(lunch)
print(dinner)
print(snack)
print(tea)
print(beer)
