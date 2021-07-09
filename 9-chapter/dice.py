from random import randint

class Dice:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        
        return(randint(1,self.sides))
    


dado_seis = Dice()
dado_diez = Dice()
dado_veinte = Dice()
dado_veinte.sides = 20
dado_diez.sides = 10
roll_six_dice = []
roll_ten_dice = []
roll_twenty_dice = []


for i in range(0,10): # dado de seis lados
    aux = dado_seis.roll_die()
    roll_six_dice.append(aux)
    
    
for i in range(0,10): # dado de 10 lados
    aux = dado_diez.roll_die()
    roll_ten_dice.append(aux)
    
    
for i in range(0,10): # dado de 20 lados
    aux = dado_veinte.roll_die()
    roll_twenty_dice.append(aux)
    
print(f'10 rolls of a 6-sided dice {roll_six_dice}')
print(f'10 rolls of a 10-sided dice {roll_ten_dice}')
print(f'10 rolls of a 20-sided dice {roll_twenty_dice}')


