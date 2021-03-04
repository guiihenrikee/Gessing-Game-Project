import random
from art import logo
print(logo)
print("Welcome do the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
dificulty = input("Choose the dificulty. Type 'easy' or 'hard': ").lower()
if dificulty == 'easy':
  guesses = 10
  print("You have 10 attempts remaining to guess the number.")
if dificulty == 'hard':
  guesses = 5
  print("You have 5 attempts remaining to guess the number.")
number = random.randint(1, 100)
guess = int(input("Make a guess: "))
while guesses >= 1:
  if guess == number:
    print("You got it! The answer was", number)
    guesses = 0
  elif guess < number:
    guesses -= 1
    print("Too low!")
    print(f"You have {guesses} attempts remaining")
    if guesses >= 1:
      guess = int(input("Guess again:"))
    else:
      print("You ran out of guesses. You lose!")
  elif guess > number:
    guesses -= 1
    print("Too high!")
    print(f"You have {guesses} attempts remaining")
    if guesses >= 1:
      guess = int(input("Guess again:"))
    else:
      print("You ran out of guesses. You lose!")



