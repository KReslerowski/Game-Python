from random import randint
from math import sqrt

class Rocket:
    def __init__(self, speed=1, altitude = 0): #kostruktor
        self.altitude = altitude
        
        self.speed = speed
        
        self.x = 0
        
    def moveUp(self):
        self.altitude += self.speed
        
    def __str__(self):
        return "Rakieta jest aktualnie na wysokosci: " + str(self.altitude)
    

class RocketBoard:
    def __init__(self, amoutOfRockets = 5):
        self.rockets = [Rocket(randint(1,6)) for _ in range(amoutOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self,key):
        return self.rockets[key]
    
    def __setitem__(self,key,value):
        self.rockets[key] = value
        
    @staticmethod
    def get_distance(self, rocket):
        ab = (rocket.altitude - self.altitude) ** 2
        bc = (rocket.x - self.x) ** 2
        
        return sqrt(ab + bc)
    
    def __len__(self):
        return len(self.rockets)