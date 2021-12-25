programming_dictionary = {
    "Bug": "An error ina programm that prevents the programm from running as expected.",
    "Function": "A piece of code that you can easily call over over again.",
    "Loop": "The action of doing something over and over again." 
}

print(programming_dictionary["Bug"])  # An error ina programm that prevents the programm from running as expected.

# Retriving items from a dictionary
print(programming_dictionary["Function"])  # A piece of code that you can easily call over over again.

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)  # {'Bug': 'An error ina programm that prevents the programm from running as expected.', 'Function': 'A piece of code that you can easily call over over again.', 'Loop': 'The action of doing something over and over again.'}

# # wIPE AN EXISTING DICTIONARY   # Commentedout for next example
# programming_dictionary = {}
# print(programming_dictionary)  # {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A mouth in my computer."
print(programming_dictionary)  # {'Bug': 'A mouth in my computer.', 'Function': 'A piece of code that you can easily call over over again.', 'Loop': 'The action of doing something over and over again.'}

# Loop through a dictionary

# for thing in programming_dictionary:  # thing just prints the key of the key value pair
    # print(thing)  # Bug
                # Function
                # Loop

for key in programming_dictionary:
    print(key)  # Bug
    print(programming_dictionary[key])  # A mouth in my computer.


                                        # Function
                                        # A piece of code that you can easily call over over again.


                                        # Loop
                                        # The action of doing something over and over again.
