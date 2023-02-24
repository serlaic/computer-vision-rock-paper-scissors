def get_computer_choice():
    import random as rd
    computer_choice = rd.choice(["Rock" , "Paper", "Scissors"])
    return computer_choice

def get_user_choice():
    user_choice = input("Choose Paper, Scissors or Rock:")
    return user_choice

def get_winner(computer_choice , user_choice):
    if computer_choice == user_choice:
        return print("It is a tie!")
    elif computer_choice == "Paper" and user_choice == "Rock":
        return print("You Lost")
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return print("You Lost.")    
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return print("You Lost.")    
    elif user_choice == "Paper" and computer_choice == "Rock":
        return print("You won!")   
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return print("You won!.")       
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return print("You won!")

get_winner(computer_choice = get_computer_choice(), user_choice = get_user_choice())



