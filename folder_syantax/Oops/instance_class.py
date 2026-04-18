# for crating constructor we are using the __init__ (here are using _init_)

class Employee:
    company= "ASUS" #This class attribute 


    # creating constructor
    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company

    def get_Salary(self):
        return self.company

e1= Employee(34000,"Akash bbol",4, "tesla")    
print(e1.company)

print(Employee.company) #print the class attruibue 


e1= Employee(34000,"Akash bbol",4, "tesla")    
print(e1.get_Salary())

'''
e2= Employee(35000,"alok bbol",3)    
print(e2.get_Salary())
'''

# object introspection to get all methods inside the class
print(dir(e1))

