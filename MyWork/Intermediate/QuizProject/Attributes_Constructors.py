# class User:
    
#     def __init__(self):
#         print("new user being created...")

# user_1 = User()  # new user being created...
# user_1.id = "001"
# user_1.username = "Richard"

# print(user_1.username)  # Richard

# user_2 = User()  # new user being created...
# user_2.id = "002"
# user_2.username = "Sandra"

# print(user_2.username)  # Sandra

'''     Attribute
Attributes are the things that the object will have
They are basically just variables that are associated with the final object'''

class Car:
    def __init__(self, seats):  # (self [is the actual object being created]: !!! seats is an added parameter. [I can add as many as I like and those parameters are going to be passed in when the object gets constructed from the class(Car)])
        self.seats = seats  # Used to set the objects attributes.

'''  my_car = Car(5)
        {Once this line of code has completed, then my_car.seats is going to be equal to five}  # ie shorthand for lines 22 and 23.
'''



class User:
    
    def __init__(self, user_id, username):  # When a new object is being constructed from this class, it must provide these two pieces of data.
        self.id = user_id
        self.username = username
        self.followers = 0  # do this for a parameter that is not always used

user_1 = User("001", "Richard")  # new user being created...
user_2 = User("001", "Sandra")

print(user_1.username)  # Richard
print(user_1.id)  # 001

# user_2 = User()  # Traceback (most recent call last):
#                 # File "c:\Users\pgold\CarlsHub\100-Days-Python\MyWork\Intermediate\QuizProject\Attributes_Constructors.py", line 42, in <module>
#                 #     user_2 = User()  # new user being created...
#                 # TypeError: User.__init__() missing 2 required positional arguments: 'user_id' and 'username'
#                 # PS C:\Users\pgold\CarlsHub\100-Days-Python> 
# user_2.id = "002"
# user_2.username = "Sandra"

# print(user_2.username)  # Sandra