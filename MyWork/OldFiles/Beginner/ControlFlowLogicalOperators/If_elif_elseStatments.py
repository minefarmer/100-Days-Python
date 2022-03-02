'''if/ elif/ else       Multiple if
if condition1:          if condition1:
    do A                    do A
elif condition2:        if condition2:
    do B                    do B
else:                   if condition3:
    do C                    do C

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
    else:
        bill = 12
        print("Adult tickets are $12.00")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
        print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
