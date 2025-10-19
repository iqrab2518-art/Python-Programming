import random

# simple hangman game

words = ["python", "program", "developer", "internship", "codealpha"]
word = random.choice(words)

guessed = []
tries = 6
display = ["_"] * len(word)

print("Welcome to Hangman!")
print("Try to guess the word. You have only 6 wrong chances.\n")

while tries > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Tries left:", tries)
    print("Guessed so far:", ", ".join(guessed))
    
    ch = input("Guess a letter: ").lower()

    if len(ch) != 1 or not ch.isalpha():
        print("Enter one valid letter!\n")
        continue
    if ch in guessed:
        print("You already tried that one!\n")
        continue

    guessed.append(ch)

    if ch in word:
        print("Good job!\n")
        for i in range(len(word)):
            if word[i] == ch:
                display[i] = ch
    else:
        tries -= 1
        print("Nope! That letter isn’t in the word.\n")

if "_" not in display:
    print("Congrats! You guessed it right ->", word)
else:
    print("Out of tries! The word was:", word)
