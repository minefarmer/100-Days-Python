# len(4837)  # Traceback (most recent call last):
            # File "/home/rich/Desktop/CarlsHub/100-Days-Python/MyWork/UnderstandingDataTypes/TypeError_Checking_Conversion.py", line 1, in <module>
            #     len(4837)
            # TypeError: object of type 'int' has no len()


# num_char = len(input("What is your name?"))  # Rich
# print("Your name has " + num_char + " characters.")  # Traceback (most recent call last):
                            # Traceback (most recent call last):
                            # File "/home/rich/Desktop/CarlsHub/100-Days-Python/MyWork/UnderstandingDataTypes/TypeError_Checking_Conversion.py", line 8, in <module>
                            #     print("Your name has " + num_char + " characters.")
                            # TypeError: can only concatenate str (not "int") to str


num_char = len(input("What is your name?"))  # Rich
# print("Your name has " + num_char + " characters.")

print(type(num_char))  # <class 'int'>
