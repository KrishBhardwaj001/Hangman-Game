import random

from word import word_list

wordlist = ['london', 'camel', 'baboon']
chosen_word = random.choice(wordlist)

lives = 6
guessed = set()

from art import logo
print(logo)

display = ["_" for letter in chosen_word]

while '_' in display and lives > 0:
    guess = input('Guess a letter: ').lower()
    
    if guess in guessed:
        print('You have already guessed it. Try again!')
        continue
    guessed.add(guess)
    
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
    if guess not in chosen_word:
        lives -= 1
    print(display)
    print(f"{lives} lives are left")  
    
if '_' not in display:
    print('You won!')
else:
    print('You lost!')  

from art import stages
print(stages[lives])