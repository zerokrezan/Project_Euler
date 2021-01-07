import math

class Vektor():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        # betrag
    def betrag(self):
        betrag = (math.sqrt((self.x**2)+(self.y**2)+(self.z**2)))
        return betrag
        # skalarprodukt
    def skalar(self,vektor2):
        skalar = ((self.x * vektor2.x) + (self.y * vektor2.y) + (self.z * vektor2.z))
        return skalar
        # kreuzprodukt
    def kreuz(self,vektor3):
        vektor3_y = (self.z * vektor3.x -self.x * vektor3.z)
        vektor3_x = (self.y * vektor3.z -self.z * vektor3.y)
        vektor3_z = ((self.x * vektor3.y)-(self.y * vektor3.x))
        kreuz =  f"Vektor{vektor3_x, vektor3_y, vektor3_z}"
        return kreuz
        
vektor1 = Vektor(2,2,2)
vektor3 = Vektor(3,3,3)
print(vektor1.kreuz(vektor3))


