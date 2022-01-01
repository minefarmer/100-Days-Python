''' Functions with output
def my_function(something):
    #Do this with something
    #Then do this
    #finally do this

def my_function():
    return 3 * 2  # result
    '''

# def format_name(f_name, l_name):

#     print(f_name.title())
#     print(l_name.title())

# format_name("rich", "MATSON")  # Rich
                                # Matson


# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     print(f"{formated_f_name} {formated_l_name}")  # Richard Matson

# format_name("RichARD", "MATSON")



def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("RichARD", "MATSON")
# print(formated_string)  # Richard Matson

print(format_name("RicHARD", "MATSON"))  # Richard Matson

output = len("Richard")
