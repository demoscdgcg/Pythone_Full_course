
# # inheritance the process of accuring properties from one class to another class is known as inheritance

# # parent class
class Animal():

    def __init__(self,name):
        self.name=name

    def spaek(self):
        print("speaking now .....")


# # inheritance here is giving the Animal access to the dog
# # child class
class Dog(Animal):

    def speak(self):
        super().spaek()
        print("woof!")
        
    


# testing
d=Dog("bruno")
d.speak()
# print(d.location)



      




