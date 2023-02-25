def get_computer_choice():
    import random as rd
    computer_choice = rd.choice(["Rock" , "Paper", "Scissors"])
    print(computer_choice)
    return computer_choice

def get_prediction():
    import time
    import cv2
    from keras.models import load_model
    import numpy as np
    start_time = time.time()
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    while True: 
        timer = time.time() - start_time
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
        print("Nothing chosen. Try again")
        get_prediction()         
# After the loop release the cap object
    cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()

def get_winner(computer_choice , user_choice):
    global computer_wins
    global user_wins
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
    get_winner(get_computer_choice(),get_prediction())

user_wins = 0
computer_wins = 0
while user_wins < 4 or computer_wins < 4:
        print("User Wins:" , user_wins)
        print("Computer Wins:" , computer_wins) 
        if user_wins == 3 or computer_wins == 3:
            break
        else:
            play()       
  