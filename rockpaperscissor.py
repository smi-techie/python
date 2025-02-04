import random  

def get_user_choice():  
    while True:  
        user_choice = input("🌟 What's your pick? (rock, paper, scissors): ").lower()  
        if user_choice in ["rock", "paper", "scissors"]:  
            return user_choice  
        else:  
            print("🚫 Oops! That's not a valid choice. Please enter rock, paper, or scissors.")  

def get_computer_choice():  
    choices = ["rock", "paper", "scissors"]  
    return random.choice(choices)  

def determine_winner(user_choice, computer_choice):  
    if user_choice == computer_choice:  
        return "🤝 It's a tie! Great minds think alike!"  
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):  
        return "🎉 You win! Nice job!"  
    else:  
        return "😢 The computer wins! Better luck next time!"  

def play_game():  
    while True:  
        user_choice = get_user_choice()  
        computer_choice = get_computer_choice()  

        print(f"You chose: {user_choice}")  
        print(f"Computer chose: {computer_choice}")  

        result = determine_winner(user_choice, computer_choice)  
        print(result)  

        play_again = input("🔄 Want to play again? (yes/no): ").lower()  
        if play_again != "yes":  
            print("👋 Thanks for playing! Have a fantastic day!")  
            break  

if __name__ == "__main__":  
    print("🎮 Welcome to Rock, Paper, Scissors! Let's have some fun!")  
    play_game()