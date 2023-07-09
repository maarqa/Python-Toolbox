import random

def randoms():
     s = random.choices('abcdefghijklmnopqrstuvwxyz', k=2)
     rand= "".join(s)
     return rand
     

for i in range(4):
     ch = input("Chose 1.Coding Or 2.Decoding:    ")
     if ch== "2" :
          coding=False
     else:
          coding= True
     encoded =""

     msg= input('PLS INPUT MSG:  ')
    
     msgl= encoded.split()
     print(msgl)
     if (coding):
          response=[]
          for i in msgl:
               if len(i) >=3:
                    new=randoms()+ i[1:] + i[0] + randoms()
                   
                    response.append(new)

               else:
                    response.append(i[::-1])
          print(" ".join(response))
     
     else: 
          response=[]
          for i in msgl:
               if len(i) >=8:
                    new= i[2:-2]
                    new1 = new[-1] + new[:-1]
                    response.append(new1)
     
               elif len(i)<= 3:
                    response.append(i[::-1])
               else: 
                    print('PLEASE TYPE VALID CODE TO DECODE')
          print(" ".join(response))
      
  
