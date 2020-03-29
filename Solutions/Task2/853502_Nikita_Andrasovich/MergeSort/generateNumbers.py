# Generate file with random numbers
import random

with open("numbers.txt",'w') as file:
    file.writelines('{}\n'.format(random.randint(-1000000,1000000)) for _ in range(5000000))