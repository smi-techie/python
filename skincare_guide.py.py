def skincare_guide():  
    """  
    Let's go through a step-by-step guide for a basic skincare routine, along with some extra tips to help you out.  
    """  
    
    print("🌟 Your Basic Skincare Routine 🌟")  
    
    # Step 1: Cleanse  
    print("1. Cleanse:")  
    print("   - Start by gently washing your face with a cleanser that suits your skin type. This is super important!")  

    # Step 2: Tone  
    print("2. Tone:")  
    print("   - Next, apply a toner to balance your skin's pH and prep it for the next steps.")  

    # Step 3: Serum  
    print("3. Serum:")  
    print("   - Time to apply a few drops of serum to target specific concerns like wrinkles or hyperpigmentation.")  
    print("      - **Tip:** Both Vitamin C and Hyaluronic Acid serums are fantastic for all skin types!")  

    # Step 4: Moisturize  
    print("4. Moisturize:")  
    print("   - Don’t forget to apply a moisturizer to keep your skin hydrated and happy.")  

    # Step 5: Sunscreen  
    print("5. Sunscreen:")  
    print("   - Finally, finish off your morning routine with a broad-spectrum sunscreen of SPF 30 or higher!")  

    # Patch Test Advice  
    print("\nImportant: Remember to do a patch test before trying out any new skincare product to avoid reactions.")  

    # Check if the user has done a patch test  
    patch_test_done = input("Have you done a patch test? (yes/no): ").strip().lower()  

    if patch_test_done == "yes":  
        skin_type = input("Great! What's your skin type? (dry/oily/mixed): ").strip().lower()  

        # Provide specific tips based on skin type  
        if skin_type == "dry":  
            print("Tip: Consider using a Hyaluronic Acid serum for that extra hydration boost.")  
        elif skin_type == "oily":  
            print("Tip: Rice water is a natural toner that can help control oil production—give it a try!")  
        elif skin_type == "mixed":  
            print("Tip: Rose water can be a lovely toner for balancing oil in your T-zone.")  
        else:  
            print("Oops! It seems you entered an invalid skin type. Please try again.")  
    else:  
        print("No worries! It's always a good idea to do a patch test when trying new products.")  

if __name__ == "__main__":  
    skincare_guide()