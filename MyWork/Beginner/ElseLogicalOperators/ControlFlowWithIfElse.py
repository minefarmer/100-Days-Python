'''water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
'''

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  # use >= if I want to include 120 cm in what is permisiable
    ''' Operator    Meaning
            >       Greater than.
            <       Lesser than.
            >=      Greater than or equal to.
            <=      Less than or equal to.
            ==      Equal to.
            !=      Not equal to.
    '''
    print("You can ride the rollarcoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''
Welcome to the rollercoaster!
What is your height in cm? 131
You can ride the rollarcoaster!

Welcome to the rollercoaster!
What is your height in cm? 105
Sorry, you have to grow taller before you can ride.
'''
