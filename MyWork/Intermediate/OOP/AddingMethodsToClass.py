'''class Car:
    def enter_race_mode():  # The name of the method.
        self.seats = 2      # Body of the method


'''

class User:
    
    def __init__(self, user_id, username):  # When a new object is being constructed from this class, it must provide these two pieces of data.
        self.id = user_id
        self.username = username
        self.followers = 0  # do this for a parameter that is not always used
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Richard")  # new user being created...
user_2 = User("002", "Sandra")

user_1.follow(user_2)
print(user_1.followers)  # 0
print(user_1.following)  # 1
print(user_2.followers)  # 1
print(user_2.following)  # 0

