class Employee:
    name="akash"

    def getSal(self):
        print(self)
        return 34000
    

# creating an object fro the class
# where e is the instance of that class
e=Employee()
print(e.getSal())

e2=Employee()
print(e2.getSal())