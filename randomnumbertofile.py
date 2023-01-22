import random
import datetime
import sys
import numpy as np
import matplotlib.pyplot as plt

# creates a file, Random.txt, and writes generated random numbers to it

with open("Random.txt", "w") as w:
    for i in range(int(input('How many random numbers?: '))):
        w.write(str(random.randint(0, 10000)))
        w.write(",")
    w.write(str(random.randint(0, 10000)))

# reads the numbers from Random.txt, and puts the mumbers into a list 

with open("Random.txt", "r") as f:
    myArray = f.read().split(",")

for i in range(0, len(myArray)):
    myArray[i] = int(myArray[i])

# uses the list, myArray, to make a histogram of the random numbers

n, bins, patches = plt.hist(myArray, 50, density=True, facecolor='r', alpha=0.75)

plt.xlabel('Random #s')
plt.ylabel('Probability')
plt.title('Random Numbers')
plt.grid(True)

plt.show()
