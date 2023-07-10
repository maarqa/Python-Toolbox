import random
import string

def password_generator(length,upper,lower,number,spchar):
     char = ""
     if upper:
          char +=string.ascii_uppercase
     if lower:
          char +=string.ascii_lowercase
     if number:
          char += string.digits
     if spchar:
          char += string.punctuation
     password = "".join(random.choice(char) for _ in range(length))
     return password


def password_str(password):
    strength = 0

    # Criteria: Length
    length = len(password)
    if length >= 8:
        strength += 1
    if length >= 12:
        strength += 2
    if length >= 16:
        strength += 1
        
    # Criteria: Complexity
    complexity = 0
    if any(char.islower() for char in password):
        complexity += 1
    if any(char.isupper() for char in password):
        complexity += 1
    if any(char.isdigit() for char in password):
        complexity += 1
    if any(char in "!@#$%^&*()-_=+[{]};:'\"<>,.?/~`" for char in password):
        complexity += 2

    strength += complexity

    # Criteria: Uniqueness
    if len(set(password)) == length:
        strength += 1

    return strength


def main():
  print("PASSWORD GENERATOR 🔐")
  print("-------------------------------")
  check = input("1. Password Generator   2.Passowrd Strength Checker:  ")
  
  if check == "2":
       check_pass = input("Enter the password you want to check:")
       print("\nNote : The password is rated from 1-10 based on its strength")
       print(password_str(check_pass))

  else:
       length= int(input("Enter the length of required passowrd:     "))
       upper = input("Include uppercase letters? (y/n): ").lower() == "y"  
       lower = input("Include lowercase letters? (y/n): ").lower() == "y"
       number = input("Include numbers? (y/n): ").lower() == "y"
       spchar = input("Include symbols? (y/n): ").lower() == "y"
       
       password = password_generator(length,upper,lower,number,spchar)
       print(f"Generated Password Is: {password}")
  
  
    
main()
  


    


