''' Nested if / else

    if condition:
        do this
    else:
        do this
    
    if another condition:
        do this
    else:
        do this
else:
    do this

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  # use >= if I want to include 120 cm in what is permisiable
    print("You can ride the rollarcoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry, you have to grow taller before you can ride.")

''' if/ elif / else

    if condition1:
        do A
    else:
        do this

'''
