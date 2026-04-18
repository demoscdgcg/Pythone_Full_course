class Restaurant:
    
    # class attribute
    restaurant_type = "Fast Food"
    
    def __init__(self, name, price):
        self.name = name      # instance attribute
        self.price = price    # instance attribute


    # ✅ INSTANCE METHOD - works with instance data (self)
    def show_item(self):
        print(f"Item: {self.name}, Price: {self.price}")


    # ✅ CLASS METHOD - works with class data (cls)
    @classmethod
    def show_type(cls):
        print(f"Restaurant Type: {cls.restaurant_type}")


    # ✅ STATIC METHOD - independent, no self or cls
    @staticmethod
    def greet():
        print("Welcome to our Restaurant!")



# ---testing---

# instance method - needs an object
item1 = Restaurant("Burger", 120)
item1.show_item()        # Item: Burger, Price: 120

# class method - can call with class directly
Restaurant.show_type()   # Restaurant Type: Fast Food

# static method - can call with class directly
Restaurant.greet()       # Welcome to our Restaurant!th