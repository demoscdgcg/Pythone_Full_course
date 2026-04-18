class Employee:
    def __init__(self, name, salary):
        self.name = name        # calls the setter automatically
        self.salary = salary

    # getter
    @property
    def name(self):
        return self._name       # returns private variable

    # setter
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty!")
        self._name = new_name   # stores in private variable


# testing
e = Employee("Jack", 34555)
print(e.name)         # Jack  ← uses getter

e.name = "Akash"      # uses setter
print(e.name)         # Akash