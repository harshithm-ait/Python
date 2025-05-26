print("Harshith Nayaka M ")
print("1AY24AI043 ")
print(" M ")
import random
streaks = 0
for _ in range(10000):
    flips = ['H' if random.randint(0,1) else 'T' for _ in range(100)]
    if 'HHHHHH' in ''.join(flips) or 'TTTTTT' in ''.join(flips):
        streaks += 1
print(f'Chance: {streaks/100}%')