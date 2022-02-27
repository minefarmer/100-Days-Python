'''
if condition1 & condition2 & condition3::
    do this
else:
    do this

Logical Operators
    A and B  # They both have to be true for the entire line of code to be true.

     C > D   # If C or D is True they will evaluate to true. Also if both are true.

      not E  # If false it becomes True, if True it becomes false.

'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  # use >= if I want to include 120 cm in what is permisiable
    print("You can ride the rollarcoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.00")
    if age <= 18:
        bill = 7
        print("Youth tickets are $7.00")
    elif age >= 45 and age <= 55:
        print("Everything is going to be OK. Have a free ride on us|")
    else:
        bill = 12
        print("Adult tickets are $12.00")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
        print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

