import time
import random
import os

i = 0

chars = ["/", "\\"]
random.seed(time.time())

os.system("cls")
os.system("color 02")

while i < 10000:
    print(random.choice(chars), end="")
    i+=1
