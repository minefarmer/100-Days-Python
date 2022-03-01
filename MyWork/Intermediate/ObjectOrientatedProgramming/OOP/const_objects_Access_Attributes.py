# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()  # a new object
print(timmy)  # <turtle.Turtle object at 0x000001514F63A410>
timmy.shape("turtle")  # changes the center into a turtle
timmy.color("coral")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)  # 300  ## the height of the screen
my_screen.exitonclick()  # This allows the screen to keep running until I click on the screen.  ## This is a method called 'exit on click'

