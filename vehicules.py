class Voiture:
    counter = 0
    def __init__(self, name, marque, vitmax, kms, color):
        self.name = name
        self.marque = marque
        self.vitmax = vitmax
        self.kms = kms
        self.color = color
        
        Voiture.counter += 1
v1 = Voiture("Serie 1", "BMW", 250, 40000, "rouge")
v2 = Voiture("Serie 2", "BMW", 150, 20000, "noire")
v3 = Voiture("Serie 3", "BMW", 150, 20000, "noire")
v4 = Voiture("Serie 4", "BMW", 150, 20000, "noire")
v5 = Voiture("Serie 5", "BMW", 150, 20000, "noire")

class Bateau:
    counter = 0
    def __init__(self, name, marque, vitmax, kms, color):
        self.name = name
        self.marque = marque
        self.vitmax = vitmax
        self.kms = kms
        self.color = color

        Bateau.counter += 1
b1 = Bateau("Yacht", "Hatteras", 40, 200, "blanc")
b2 = Bateau("Yacht", "Hatteras", 40, 200, "blanc")


class Moto:
    counter = 0
    def __init__(self, name, marque, vitmax, kms, color):
        self.name = name
        self.marque = marque
        self.vitmax = vitmax
        self.kms = kms
        self.color = color

        Moto.counter += 1
m1 = Moto("Burgman Suzuki", "Suzuki", 2000, 200, "bleue")
m2 = Moto("Burgman Suzuki", "Suzuki", 2000, 200, "bleue")
m3 = Moto("Burgman Suzuki", "Suzuki", 2000, 200, "bleue")

class Avion:
    counter = 0
    def __init__(self, name, marque, vitmax, kms, color):
        self.name = name
        self.marque = marque
        self.vitmax = vitmax
        self.kms = kms
        self.color = color

        Avion.counter += 1
a1 = Avion("Boeing 737", "Boeing", 20000, 500, "rouge et blanc")