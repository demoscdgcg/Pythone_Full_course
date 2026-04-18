
class Employee:

    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    
    # writtint another magic method __str__
    def __str__(self):
        return f"The name is {self.name} and the salry is {self.sal}"


    # writtint another magic method __repr__
    def __repr__(self):
        return f"The name is {self.name} and the salry is {self.sal}"
  

p=Employee("akash",24)
print(p.name,p.sal)        
print(str(p))
print(repr(p))