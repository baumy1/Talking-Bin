# Import dependecies, gpiozero for button, os to run commands in the terminal and random for obvious reasons
from gpiozero import Button
import os
import random

# Define the button using GPIO 2 (Pin 3)
button = Button(2)
# This variable requires the flap to be closed again before a sound can play again
hasPlayed = False

# Main loop for the script, repeats as often as possible
while True:

    # If the flap is open
    if not button.is_pressed:
        # If the flap is not being held open
        if not hasPlayed:
            print("Not Pressed!")

            # Choose a random number that will be played 
            file_number = random.randint(1, 38)

            print ('Playing file ' + str(file_number))

            # Play the sound by running a command in the terminal
            os.system('omxplayer -o local /home/pi/Desktop/Bin_Sounds/' + str(file_number) + '.wav')

            # Stops the sound from playing again until this is false 
            hasPlayed = True

    # If the flap is closed
    if button.is_pressed:
        print("Pressed")
        # Allows the sound to be played again
        hasPlayed = False
