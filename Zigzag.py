print("Harshith Nayaka M ")
print("1AY24AI043 ")
print(" M ")
import time
indent = 0
increase = True
while True:
    print(' ' * indent + '********')
    time.sleep(0.1)
    if increase:
        indent += 1
        if indent == 20:
            increase = False
    else:
        indent -= 1
        if indent == 0:
            increase = True