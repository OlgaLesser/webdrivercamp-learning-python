#!C:\Users\korch\AppData\Local\Programs\Python\Python312
import random
random_num = random.randint(-10, 10)
if random_num < 0:
    print(str(random_num) + " is negative")
elif random_num > 0:
    print(str(random_num) + " is positive")
else:
    print(str(random_num) + " is zero")
