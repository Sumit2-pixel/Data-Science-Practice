# Projec: Number Guessing Game

import random
comp_choice = random.randint(1, 10)

attempts = 0

while True:

   user_guess = int(input("Guess a number between 1 to 10:"))
   attempts += 1
   
   if user_guess  == comp_choice:
       print(f"Correct you guessed in {attempts} attempts:")
       break
   else:
       print("Try agian")

# Computer selects a random number
# Loops run until user guess corretly
# Attempts counter track tries





