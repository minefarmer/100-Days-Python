#  Object ::  Class
#    car = CarBluePrint()

# import another_module

# print(another_module.another_variable)  # 12


from turtle import Turtle, Screen  ## the screen represents the window in which the turtle is going to show up

timmy = Turtle()
# print(timmy)  # <turtle.Turtle object at 0x7f471b5300d0>  ## an object has been printed at (memory location)

#  Object  .  Attribute
      # car.speed

# my_screen = Screen()
# print(my_screen.canvheight)  # <turtle.Turtle object at 0x7f6555b200d0>
                             # 300


# car     attributes:  =  speed - 0


#                     def move():
#                         speed = 60
#             does:           # functions
#                     def stop():
#                         speed = 0

timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight) 
my_screen.exitonclick()