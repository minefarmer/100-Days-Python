''' Functions with more than one parameter.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Somewhere")  # Hello Jack Bauer
                                        # What is it like in Somewhere
'''

""" Keyword Arguments  ## used to change the order of the arguments
def my_function(a, b, c):
    # do this with a            a = 3
    # do this with b            b = 1
    # finnaly do this with c    c = 2

"""

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name="Rich", location="Bertrand")  # Hello Rich
                                            # What is it like in Bertrand?

