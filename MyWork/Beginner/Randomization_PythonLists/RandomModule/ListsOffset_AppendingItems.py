'''     Lists
Lists use square brackets []

import random

randomIntergeter = random.randint(1, 10)
print(randomIntegeter)

randomFloat= random.random() * 5
print(randomfloat)

love_score = random.randint(1, 100)
print(f:Your love score is {love_score})

'''

# fruits = ["Cherry", "Apple", "Pear"]

states_of_America = ["Delaware","Pensylvania"]

print(states_of_America[0])  # Delaware
print(states_of_America[1])  # Pensylvania
print(states_of_America[-1])  # Pensylvania
print(states_of_America[-2])  # Delaware

states_of_America[1] = "Nebraska"
print(states_of_America)  # Nebraska

states_of_America.append("Angelaland")
print(states_of_America)  # ['Delaware', 'Nebraska', 'Angelaland']
