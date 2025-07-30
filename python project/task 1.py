import random

def hangman():
    word_list = ['python', 'hangman', 'programming', 'artificial', 'intelligence', 'data', 'science']
    word = random.choice(word_list).lower()
    guessed_letters = []
    attempts = 6  # Number of allowed wrong guesses

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        # Display current state of word
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(display_word))

        if '_' not in display_word:
            print(f"Congratulations! You guessed the word '{word}'.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
hangman()

