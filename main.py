import random

# Define available clothing items
clothing_items = {
    'tops': ['T-shirt', 'Blouse', 'Sweater', 'Tank Top'],
    'bottoms': ['Jeans', 'Skirt', 'Shorts', 'Leggings'],
    'shoes': ['Sneakers', 'Sandals', 'Boots', 'Heels'],
    'accessories': ['Hat', 'Scarf', 'Necklace', 'Bracelet']
}

# Function to display options
def display_options(category):
    print(f"\nChoose a {category}:")
    for i, item in enumerate(clothing_items[category], start=1):
        print(f"{i}. {item}")

# Function to get user choice
def get_choice(category):
    while True:
        try:
            choice = int(input(f"Enter the number for your choice of {category}: "))
            if 1 <= choice <= len(clothing_items[category]):
                return clothing_items[category][choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(clothing_items[category])}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main game function
def dress_up_game():
    print("Welcome to the Dress-Up Game!")
    
    # Get user choices
    chosen_outfit = {}
    for category in clothing_items:
        display_options(category)
        chosen_outfit[category] = get_choice(category)
    
    # Randomly generate a compliment
    compliments = [
        "You look fantastic!",
        "What a great choice!",
        "That outfit really suits you!",
        "You're a fashion icon!"
    ]
    random_compliment = random.choice(compliments)

    # Display the chosen outfit and compliment
    print("\nYour chosen outfit:")
    for category, item in chosen_outfit.items():
        print(f"{category.capitalize()}: {item}")
    
    print(random_compliment)

# Run the game
if __name__ == "__main__":
    dress_up_game()
