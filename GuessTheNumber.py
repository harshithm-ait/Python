print("Your Name, Your USN, Your Section")
import random
number = random.randint(1, 20)
print("Guess between 1-20:")
for guesses in range(1, 7):
    guess = int(input())
    if guess == number:
        print(f"Correct! in {guesses} tries!")
        break
    print("Too high" if guess > number else "Too low")
else:
    print(f"Number was {number}")