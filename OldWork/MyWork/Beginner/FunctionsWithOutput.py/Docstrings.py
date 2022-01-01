def format_name(f_name, l_name):
    """ This is a docstring.   Take the first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return  "You didn't provide valid inputs."  # Whenno valid inputs are given == this exits the function
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
