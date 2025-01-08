from words import random_words
import random
from art import logo, stages

lives = len(stages) - 1
chosen_word = random.choice(random_words) # random.choice() picks a random item from a list
print(f"Chosen word: {chosen_word}")

print(logo)

blanks = ["_" for _ in chosen_word] # Create a list of underscores based on the length of the chosen_word
print(" ".join(blanks))

while "_" in blanks and lives != 0:
    guessed_letter = input("\nGuess a letter: ").lower()
    if guessed_letter in chosen_word:
        # Loop through the chosen_word and check if the guessed_letter is in the chosen_word
        for index, letter in enumerate(chosen_word):
            if letter == guessed_letter:
                blanks[index] = guessed_letter # Replace the underscore with the guessed_letter if it's correct
    else:
        print(stages[lives])
        lives -= 1
    print(" ".join(blanks))

if "".join(blanks) == chosen_word:
    print("\nYou win!")
