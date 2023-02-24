def get_computer_choice():
    import random as rd
    computer_choice = rd.choice(["Rock" , "Paper", "Scissors"])
    return computer_choice

def get_user_choice():
    user_choice = input("Choose Paper, Scissors or Rock:")
    return user_choice

def get_winner(computer_choice , user_choice):
    if computer_choice == user_choice:
        return "It is a tie!"
    elif computer_choice == "Paper" and user_choice == "Rock":
        return "You Lost"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return "You Lost"    
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return "You Lost"   
    elif user_choice == "Paper" and computer_choice == "Rock":
        return "You won!"  
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return "You won!"       
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return "You won!"

print(get_winner(get_computer_choice() , get_user_choice()))




