import random

def get_quotes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            quotes = [line.strip() for line in lines]
            return quotes
    except FileNotFoundError:
        print("Error: Quotes file not found.")
        return []

def display_random_quote(quotes):
    if quotes:
        random_quote = random.choice(quotes)
        print("Random Quote:")
        print(random_quote)
    else:
        print("No quotes available.")



file_path = "quotes.txt"
quotes = get_quotes_from_file(file_path)

while True:
        user = input("Press any key to display a random quote (or 'q' to quit): ")
        if user.lower() == 'q':
            break
        print("--------::----------")
        display_random_quote(quotes)
        print("--------::----------")
        
        
