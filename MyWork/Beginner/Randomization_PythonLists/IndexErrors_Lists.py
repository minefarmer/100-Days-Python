# states_of_America = ["Delaware","Pensylvania"]
# states_of_America.append("Nebraska", "Kansas")

# print(states_of_America)  # Traceback (most recent call last):
                            # File "/home/rich/Desktop/CarlsHub/100-Days-Python/MyWork/Randomization_PythonLists/IndexErrors_Lists.py", line 2, in <module>
                            #     states_of_America.append("Nebraska", "Kansas")
                            # TypeError: append() takes exactly one argument (2 given)


# states_of_America = ["Delaware","Pensylvania"]
# print(states_of_America)

# states_of_America.append("Nebraska")
# states_of_America.append("Kansas")
# print(states_of_America)  # ['Delaware', 'Pensylvania', 'Nebraska', 'Kansas']

# print(len(states_of_America))  # 4

# # print(states_of_America[num_of_states])  # Traceback (most recent call last):
#                                         # File "/home/rich/Desktop/CarlsHub/100-Days-Python/MyWork/Randomization_PythonLists/IndexErrors_Lists.py", line 19, in <module>
#                                         #     print(states_of_America[num_of_states])
#                                         # NameError: name 'num_of_states' is not defined

# num_of_states = len(states_of_America)

# print(states_of_America[num_of_states - 1])  # Kansas



# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peachs", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)  # [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]


