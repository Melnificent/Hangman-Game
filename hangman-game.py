import random

words = ["pizza", "burger", "salad", "donut", "sushi", "pasta"]
word = words[random.randrange(len(words))]
letters = []

print("Welcome to Hangman!")
life = 6
while life < 10:
    guess = input("Guess the right letter: ")
    if guess in word:
        print("Wow! You got it right!")
        letters.append(guess)
        if len(letters) == len(word):
            print("Congratulations! You won :)")
            break
        else:
            letters_left = len(word) - len(letters)
            print(f"You have {letters_left} letters left.")
    else:
        life -= 1
        if life == 0:
            print("Game Over! :()")
            break
        else:
            print(f"Wrong letter! You have {life} lives left.")
