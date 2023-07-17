gameover = False
def ttt_table(value):
     print(f'''
           |      |
       {value[1]}   |  {value[2]}   |  {value[3]}
     ______|______|______
           |      |
       {value[4]}   |  {value[5]}   |  {value[6]}
     ______|______|______
           |      |
       {value[7]}   |  {value[8]}   |  {value[9]}
           |      | ''')


               
def check_win(value,current):
     global gameover
     if value[1]==value[2]==value[3] =="X": 
               gameover= True
     if value[4]==value[5]==value[6] =="X":
               gameover= True
     if value[7]==value[8]==value[9] =="X":
               gameover= True
     if value[1]==value[4]==value[7] =="X":
               gameover= True
     if value[2]==value[5]==value[8] =="X":
               gameover= True
     if value[3]==value[6]==value[9] =="X":
               gameover= True
     if value[1]==value[5]==value[9] =="X":
               gameover= True
     if value[3]==value[5]==value[7] =="X":
               gameover= True
     if value[1]==value[2]==value[3] =="O":
               gameover= True
     if value[4]==value[5]==value[6] =="O":
               gameover= True
     if value[7]==value[8]==value[9] =="O":
               gameover= True
     if value[1]==value[4]==value[7] =="O":
               gameover= True
     if value[2]==value[5]==value[8] =="O":
               gameover= True
     if value[3]==value[6]==value[9] =="O":
               gameover= True
     if value[1]==value[5]==value[9] =="O":
               gameover= True
     if value[3]==value[5]==value[7] =="O":
               gameover= True
     
     return gameover
    
def run(name1 , name2):
     value=[" "," "," "," "," "," "," "," "," "," "]     
     current = name1
     ttt_table(value)
     while not gameover: 
          print(f" Your Turn {current}")
          
          print("Choose The cell no.")
          data = int(input("1-9:    "))
          value[data] = ("X" if current==name1 else "O")
          ttt_table(value)
          check_win(value,current)
          if gameover:
               
               print(f"You successfully Won! {current}")
          if current==name1:
               current =name2 
          else:
               current=name1

print("\t \t \t Tic Tac Toe 🎮")
print("Player 1 Type your name:")
name1 = input()
print("Player 2 Type your name:")
name2 = input()
run(name1,name2)
