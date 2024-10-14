
from random import random, randint

while True:
    user_input = input("Roll a dice(y/n): ").lower()
    if user_input == 'y':
        num1 = randint(1, 6)
        num2 = randint(1, 6)
        print(num1, num2)
    elif user_input== 'n':
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
