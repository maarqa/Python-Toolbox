import random

for i in range(4):
   print('''Snake Water Gun Game 🎮
-------------------
''')
   pl = int(input("Chose the point:\n1. Snake     2.Water     3.Gun      "))
   cm = random.randint(1,3)
  
   
   if pl== 1 and cm == 1:
      print("Player Chose  Snake and Computer Chose Snake")
      print("Draw")
   elif pl== 1 and cm == 2:
      print("Player Chose  Snake and Computer Chose Water")
      print("Player Won")
   elif pl== 1 and cm == 3:
      print("Player Chose  Snake and Computer Chose Gun")
      print("Computer Won")
   elif pl== 2 and cm == 1:
      print("Player Chose Water and Computer Chose Snake")
      print("Computer Won")
   elif pl== 2 and cm == 2:
      print("Player Chose Water and Computer Chose Water")
      print("Draw")
   elif pl== 2 and cm == 3:
      print("Player Chose Water and Computer Chose Gun")
      print("Player Won")
   elif pl== 3 and cm == 1:
      print("Player Chose  Gun and Computer Chose Snake")
      print("Player Won")
   elif pl== 3 and cm == 2:
      print("Player Chose Gun and Computer Chose Water")
      print("Computer Won")
   elif pl== 3 and cm == 3:
      print("Player Chose Gun and Computer Chose Gun")
      print("Draw")
   print("\n")
    
