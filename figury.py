class Rectangle:
    def __init__(self, bokA, bokB):
        self.bokA = bokA
        self.bokB = bokB

    def powierzchnia(self):
        wynik = self.bokA * self.bokB
        return wynik
    
class Square(Rectangle):
    def __init__(self,bok):
        super().__init__(bok, bok)
        

class Cube(Square):
    def powierzchnia(self):
       return  super().powierzchnia() * 6
        

cube = Cube(2)

print(cube.powierzchnia())