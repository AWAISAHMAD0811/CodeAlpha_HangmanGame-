
import random

# Step 1: Define words
word_list = ['apple', 'banana', 'orange', 'grape', 'mango']
secret_word = random.choice(word_list)

# Step 2: Initialize variables
guessed_letters = []
attempts_left = 6
display_word = ['_'] * len(secret_word)

# Step 3: Game loop
while attempts_left > 0 and '_' in display_word:
    print("\nCurrent word: " + ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    print("Attempts left:", attempts_left)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct guess!")
    else:
        attempts_left -= 1
        print("Wrong guess!")

# Step 4: Game result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 You lost! The word was:", secret_word)
