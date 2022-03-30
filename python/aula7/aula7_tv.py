
class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == False:
            self.ligada = True
        elif self.ligada == True:
            self.ligada = False

    def aumentaCanal(self):
        if self.ligada == True:
            self.canal += 1

    def diminuiCanal(self):
        if self.ligada == True:
            self.canal -= 1


tv = TV()
print('A TV está ligada?: {}' .format(tv.ligada))
tv.power()
print('A TV está ligada?: {}' .format(tv.ligada))
print('Canal: {}' .format(tv.canal))
tv.aumentaCanal()
tv.aumentaCanal()
print('Canal: {}' .format(tv.canal))
tv.diminuiCanal()
print('Canal: {}' .format(tv.canal))
tv.power()
print('A TV está ligada?: {}' .format(tv.ligada))
