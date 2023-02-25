def get_computer_choice():
    '''
    This function is used to create a random choice from the list ["Rock" , "Paper", "Scissors"]

    Parameters:
    ----------
        computer_choice(string): Random computer choice
    '''
    import random as rd
    computer_choice = rd.choice(["Rock" , "Paper", "Scissors"])
    print(computer_choice)
    return computer_choice

def get_prediction():
    '''
    This function is used to capture an image from the user

    Returns string "Rock","Paper,"Stone" depending on the last image captured upon the 10 second timer expiration

    Imports:
    --------

    time
    cv2
    keras.models
    numpy

    Parameters:
    ----------
        start_time(float): saves current time into a variable
        model(keras.engine.sequential.Sequential): loads model from "keras_model.h5" file
        cap(cv2.Videocapture): --read documentation on cv2--
        data(numpy.ndarray): --read documentaiton on numpy--
        timer(float): counts the time starting from start_time
        frame(numpy.ndarray): --read documentaiton on numpy--
        resized_frame(numpy.ndarray): --read documentaiton on numpy-- 
        image_np(numpy.ndarray): --read documentaiton on numpy--
        prediction(numpy.ndarray): gives percentage of prediction depending on which model user is showing(Rock,Paper,Scissors or Nothing)
        user_choice(numpy.int64): returns the indices of the maximum values along an axis from prediction
    '''
    import time
    import cv2
    from keras.models import load_model
    import numpy as np
    start_time = time.time()
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    while True:
# Starts the timer
        timer = time.time() - start_time
# Breaks the while loop when timer reaches 10 seconds
        if timer > 10:
            break
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        user_choice = np.argmax(prediction)
# Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Returns Rock, Paper or Scissors strings depending on the user_choice output
    if user_choice == 0:
        print("Rock")
        return "Rock"
    elif user_choice == 1:
        print("Paper")
        return "Paper"
    elif user_choice == 2:
        print("Scissors")
        return "Scissors" 
    elif user_choice == 3:
# Repeats the function get_prediction to get the prediction again if user didn't show anything 
        print("Nothing chosen. Try again")
        get_prediction()         
# After the loop release the cap object
    cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()

def get_winner(computer_choice , user_choice):
    '''
    This function is used to decide who is a winner between the player and computer

    Returns the print function with a string inside depending on the computer_choice or user_choice

    Arguments:
    -----------
        computer_choice(string): Random computer choice
        user_choice(string): User choice captured from the webccam

    Parameters:
    ----------
        computer_wins(int): Number of computer win
        user_wins(int): Number of user wins
    '''
    global computer_wins
    global user_wins
# Statements to decide who is the winner between the computer and the player
    if computer_choice == user_choice:
        return print("It is a tie!")
    elif computer_choice == "Rock" and user_choice == "Scissors":
        computer_wins += 1
        return print("You lost")
    elif computer_choice == "Paper" and user_choice == "Rock":
        computer_wins += 1
        return print("You lost") 
    elif computer_choice == "Scissors" and user_choice == "Paper":
        computer_wins += 1
        return print("You lost")  
    else:   
        user_wins += 1 
        return print("You won!")    

def play():
    '''
    This function calls get_winner function with 2 arguments which are returns from get_computer_choice and get_prediction functions
    '''
    get_winner(get_computer_choice(),get_prediction())

# While loop to play the game until player or computer has 3 wins in total
user_wins = 0
computer_wins = 0
while user_wins < 4 or computer_wins < 4:
        print("User Wins:" , user_wins)
        print("Computer Wins:" , computer_wins) 
        if user_wins == 1 or computer_wins == 1:
            break
        else:
            play()       
  