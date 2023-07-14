import random

words = ["Head", "Apple", "Bat", "Cat", "Dog", "Eat", "Turtle", "Fish", "Jug", "Jet", "Zebra", "Happy", "Mill", "Chill", "Bill", "Drill", "Sleep", "Sit"]

def game():
    chosen_word = random.choice(words).lower()
    word_letters = list(chosen_word)
    guessed_letters = ['_'] * len(chosen_word)
    print(guessed_letters)

    for attempt in range(1, 11):
        guess = input("Guess a letter: ").lower()

        if guess in word_letters:
            print("Correct!")
            indices = [i for i, letter in enumerate(word_letters) if letter == guess]
            for index in indices:
                guessed_letters[index] = guess
            print(guessed_letters)
        else:
            print("Wrong! Try Again.")
            print(guessed_letters)

        if guessed_letters == word_letters:
            print(f"You Won in {attempt} tries!")
            return

    print("You Lost. The word was:", chosen_word)


print("Word Guess Game 🎮")
print("---------------------------")
game()
