import random as rd

def get_computer_choice():
    computer_choice = rd.choice(['Rock' , 'Paper', 'Scissors'])
    return computer_choice

def get_user_choice():
    user_choice = input('Choose Paper, Scissors or Rock')
    return user_choice



