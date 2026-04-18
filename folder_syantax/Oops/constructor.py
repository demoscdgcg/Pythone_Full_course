# for crating constructor we are using the __init__ (here are using _init_)

class Employee:

    # creating constructor
    def __init__(self,salary,name,born):
        self.salary=salary
        self.name=name
        self.born=born

    def get_Salary(self):
        return self.salary

e1= Employee(34000,"Akash bbol",4)    
print(e1.get_Salary())

e2= Employee(35000,"alok bbol",3)    
print(e2.get_Salary())

