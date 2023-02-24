# Computer Vision RPS

## Rock Paper Scissors Game

### Steps creating computer vision system using teachable machine project

* Teachable machine trains a computer to detect whether the user is showing Rock, Paper, Scissors to the camera.
* Creates 4 different classes: Rock, Paper, Scissors and Nothing
* Trains module using default parameters
    * Epochs : 50
    * Batch Size : 16
    * Learning Rate: 0.001
* Exporting model filename: keras_model.h5 which contains a structure and the parameters of deep learning model.
* Model will be used in a future project for game called Rock Paper Scissors where the user will be able to show his choice to the camera.
* Python Programming Language will be used in this projects

### Dependencies

* Python 3.8 Environment
* Conda environement packages installed
    * opencv-python
    * tensorflow
    * ipykernel
* Full details can be found in requirements.txt file

### Rock Paper Scissors game manual script information

*manual_rps.py file contains the skript for the game without the computer vision system. I'ts a manual version of the game where computer choice is made randomly and user inputs the choice manually*

* def_computer_choice makes a random choice for computer
* def_user_choice asks user to choose Rock, Paper or Scissors
* get_winner checks who is a winner in a game and returns the string: 'I'ts a tie', 'You won!' or 'You lost'
* play function calls all the functions above 
