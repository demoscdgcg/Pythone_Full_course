class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self,p):
        return Point((self.x + p.x), (self.y +p.y))

  