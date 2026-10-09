import random

words = ["pizza", "burger", "salad", "donut", "sushi", "pasta"]
word = words[random.randrange(len(words))]
letters = []

print("Welcome to Hangman!")
life = 6
while life < 10:
    guess = input("Guess the right letter: ")
    if guess in word:
        if guess in letters:
            print("You already guessed that!")
        else:
            print("Wow! You got it right!")
            letters.append(guess)
            letters_left = 0
            for char in word:
                if char not in letters:
                    letters_left +=1
        if letters_left == 0:
            print("Congratulations! You won :)")
            break
        else:
            print(f"You have {letters_left} letters left.")
    else:
        life -= 1
        if life == 0:
            print("Game Over! :()")
            break
        else:
            print(f"Wrong letter! You have {life} lives left.")
