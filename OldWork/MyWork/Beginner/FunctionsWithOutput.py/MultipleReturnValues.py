# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#     print("This got printed")

# print(format_name("RicHARD", "MATSON"))  # Richard Matson



# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#     print("This got printed")  # This was not printed because the return is the end of the function

# print(format_name("RicHARD", "MATSON"))  # Richard Matson



# def format_name(f_name, l_name):
#     # if f_name == "" or l_name == "":

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))  # What is your first name? RICH
                                                                                             # What is your last name? matson
                                                                                             # Rich Matson


# def format_name(f_name, l_name):
#     # if f_name == "" or l_name == "":

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))  # What is your first name? 
                                                                                           # What is your last name? 
                                                                                           # Result:



# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return  # This escapes the function if no names are entered and None is the last output
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))  # What is your first name? 
                                                                                            # What is your last name? 
                                                                                            # None



def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return  "You didn't provide valid inputs."  # Whenno valid inputs are given == this exits the function
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))  # What is your first name? 
                                                                                        # What is your last name? 
                                                                                        # You didn't provide valid inputs.
