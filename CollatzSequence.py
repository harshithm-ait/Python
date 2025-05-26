print("Harshith Nayaka M ")
print("1AY24AI043 ")
print(" M ")
def collatz(number):
    while number != 1:
        print(number)
        number = number // 2 if number % 2 == 0 else 3 * number + 1
    print(1)
collatz(int(input("Enter number: ")))