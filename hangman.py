import random

words = ["python", "computer", "programming", "developer", "keyboard"]

word = random.choice(words)

display = ["_"] * len(word)

attempts = 6

while attempts > 0:

    print("\nWord:", "".join(display))
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct guess")

        i = 0

        while i < len(word):
            if word[i] == guess:
                display[i] = guess

            i += 1

    else:
        print("Wrong guess")
        attempts -= 1
        
    if "_" not in display:
        print("\nCongratulation! / You win")
        break 

    if attempts==0:
        print("\nGame over")
        print("The word was:", word)
        