print('''Welcome to Morse Code Interpreter 🖥️
-------------------------''')
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-','5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--','?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.','$': '...-..-', '@': '.--.-.', ' ': '/'}
while True:
     print('''
Enter Your Choice:
1. Generate Morse Code
2. Read Morse Code
''')
     response =input()
     if response =="1":
          text = input("Enter Text To Convert To Morse Code:\t").upper()
          text = text.upper()        
          code = [morse.get(char, '') for char in text]       
          code = ' '.join(code)
          print(code)
     else:
          text = input("Enter Morse Code to Convert To Text:\t")
          decode =[]
          lis = text.split()
          for char in lis:
               for key , value in morse.items():
                    if char==value:
                         decode.append(key)
          print("".join(decode))
    
