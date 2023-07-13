import random

def roller(dices, sides):  
    rolls = f"{random.randint(1,sides)}"
    for i in range(dices-1):
        roll = random.randint(1, sides)
        rolls += f",{roll}"
    return rolls

    
while True:        
     
    print("\nDice Roller 🎲")
    print("-------------------")
    dices = int(input("Numbers of dice to roll: "))
    sides = int(input("Number of sides on each die: "))
    rolls = roller(dices, sides)
    print("Please Wait \n    Rolling...")
    print("The results are:", rolls)
    

