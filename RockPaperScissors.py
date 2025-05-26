print("Harshith Nayaka M ")
print("1AY24AI043 ")
print("M ")
import random
choices = ['rock', 'paper', 'scissors']
user = input("Enter choice: ").lower()
comp = random.choice(choices)
print(f"Computer chose {comp}")
if user == comp:
    print("Tie!")
elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
    print("You win!")
else:
    print("You lose!")