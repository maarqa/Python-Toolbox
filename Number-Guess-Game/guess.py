import random


guess = random.randint(1,10)
print(guess)
print('''This is a Guess Game
You are having five chances to guess the right no.
''')
z =0
for i in range(5):
     print("Please Enter the guessed no b/w 1-10:")
     z +=1
     result = int(input())
     if result < guess:
          print("Too Low")     
     elif result > guess:
          print("Too High")
     else:
          break
print(f"Congrats 🎉 You guessed right in {z} attemps") if guess == result else print("Sorry 😔 , You failed")
      
