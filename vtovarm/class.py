class Mom():
    def __innit__(self, eyes, iq, hair):
        self.eyes_s = eyes
        self.iq_s = iq
        self.hair_s = hair

    def __init__(self):
        print(f'Eyes {self.eyes_s}')
        print(f'IQ {self.iq_s}')
        print(f'Hair {self.hair_s}')

class Daughter(Mom):
    def __init__(self, eyes, iq, hair, profesion='Ing.'):
        Mom.__init__(eyes, iq, hair)
        self.profession = profesion

mama = Mom('Marron', 120, 'Marron')
hija = Daughter('Marron', 120, 'Marron')

mama.mostrar_info()
hija.mostrar_info()

print(hija.profesion)
