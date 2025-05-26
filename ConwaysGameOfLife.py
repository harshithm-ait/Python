print("Harshith Nayaka M ")
print("1AY24AI043 ")
print(" M ")
import random, time
width = 20
height = 10
board = [[random.choice([0,1]) for _ in range(width)] for _ in range(height)]
while True:
    for row in board:
        print(''.join(['#' if cell else ' ' for cell in row]))
    time.sleep(0.5)
    # Add game logic here
    break  # Remove this for actual implementation