from random import randint

random = randint(1, 100)
while True:
    try:
     user_guess = int(input("Guess the number between 1 and 100: "))
     if user_guess < 100:
         if user_guess == random:
             print("Number matched")
             break
         elif user_guess > random:
             print("Too high!")
         elif user_guess < random:
             print("Too low!")
     elif user_guess>100:
         print("Please enter a number less than 100")

    except ValueError as e:
        print("Please enter a valid number")


