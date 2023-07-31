import random

name = input("Enter name: ")
print(f"Welcome {name}, time to play hangman!")

secret_Word = ("eminem","metallica","2pac","haarper","quenn","zhu")
word = random.choice(secret_Word)

guess_string = ""

lives = 10

guessed_letters = set()

while lives > 0:

    character_left = 0

    for character in word:

        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left += 1

    if character_left == 0:
        print("YOU WON!!")
        break 

    guess = input("Guess a letter: ")

    if len(guess) != 1:
        print("Please enter only 1 letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    
    guessed_letters.add(guess)
    guess_string += guess

    if guess in word:
        print("Correct guess!")

    if guess not in word:
        lives -= 1
        print("Wrong guess!")
        print(f"You have {lives} left")

        if lives == 0:
            print ("You died!")
            break