class Recipe:  
    def __init__(self, name, ingredients, instructions):  
        self.name = name  
        self.ingredients = ingredients  
        self.instructions = instructions  

    def display(self):  
        print(f"\n### 🍽️ {self.name} ###")  
        print("**Ingredients:**")  
        for ingredient in self.ingredients:  
            print(f"- {ingredient}")  
        print("**Instructions:**")  
        print(self.instructions)  

    def get_nutritional_benefits(self, ingredient):  
        benefits = {  
            "chicken": "High in protein and low in fat, excellent for muscle growth.",  
            "curry powder": "Contains anti-inflammatory properties and antioxidants.",  
            "onion": "Rich in vitamins and antioxidants, great for heart health.",  
            "garlic": "Boosts the immune system and has antibacterial properties.",  
            "tomato": "High in vitamin C and lycopene, good for skin health.",  
            "cheese": "A source of calcium and protein but should be consumed in moderation.",  
            "basil": "Rich in vitamins and antioxidants, may help with inflammation.",  
            "olives": "High in healthy fats and antioxidants, beneficial for heart health.",  
            "flour": "Source of carbohydrates, good for energy, but can be high in calories."  
        }  

        return benefits.get(ingredient.lower(), "Hmm, I don’t have the nutritional information for that ingredient.")  

def display_main_menu():  
    print("\n--- Welcome to Your Recipe Book! ---")  
    print("1. View Chicken Curry Recipe")  
    print("2. View Italian Pizza Recipe")  
    print("3. Add a Custom Recipe")  
    print("4. Exit")  

def main():  
    # Predefined recipes  
    chicken_curry = Recipe(  
        "Chicken Curry",  
        ["Chicken", "Curry Powder", "Onion", "Garlic", "Tomato", "Salt", "Oil"],  
        "1. Heat oil in a pan. 2. Add chopped onions and garlic, sauté until golden. "  
        "3. Add chicken pieces and cook until browned. 4. Sprinkle curry powder and cook for a minute. "  
        "5. Add chopped tomatoes, salt, and simmer until chicken is cooked through."  
    )  

    italian_pizza = Recipe(  
        "Italian Pizza",  
        ["Dough", "Tomato Sauce", "Cheese", "Basil", "Olives"],  
        "1. Preheat your oven to 475°F (245°C). 2. Roll out the dough. 3. Spread tomato sauce over the dough. "  
        "4. Add cheese, basil, and olives. 5. Bake for 10-12 minutes until the crust is golden."  
    )  

    # Display predefined recipes  
    chicken_curry.display()  
    italian_pizza.display()  

    while True:  
        display_main_menu()  
        choice = input("What would you like to do? (1-4): ")  

        if choice == '1':  
            print("\nGreat choice! Here's the Chicken Curry recipe:")  
            chicken_curry.display()  
        elif choice == '2':  
            print("\nMamma Mia! Here's the Italian Pizza recipe:")  
            italian_pizza.display()  
        elif choice == '3':  
            print("\nAwesome! Let’s add your custom recipe.")  
            name = input("What’s the name of your recipe? ")  
            ingredients = input("List the ingredients separated by commas: ").split(",")  
            instructions = input("How do you prepare it? ")  
            custom_recipe = Recipe(name.strip(), [ingredient.strip() for ingredient in ingredients], instructions)  
            print("\nHere’s your custom recipe:")  
            custom_recipe.display()  
        elif choice == '4':  
            print("Thanks for stopping by! Happy cooking! Goodbye! 👋")  
            break  
        else:  
            print("Oops! That didn't seem like a valid choice. Please try again.")  

        # Ask if the user wants nutritional benefits  
        nutrient_query = input("Would you like to know the nutritional benefits of any ingredient? (yes/no): ").strip().lower()  
        if nutrient_query == 'yes':  
            ingredient = input("Please enter the ingredient name: ").strip()  
            benefits = (custom_recipe.get_nutritional_benefits(ingredient) if 'custom_recipe' in locals()  
                        else chicken_curry.get_nutritional_benefits(ingredient) or italian_pizza.get_nutritional_benefits(ingredient))  
            print(f"\n✨ Nutritional Benefits of {ingredient.capitalize()}: {benefits}")  

if __name__ == "__main__":  
    main()