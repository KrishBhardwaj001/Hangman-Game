# Hangman Game

A simple Python implementation of the classic **Hangman** game. Guess the letters of a hidden word within a limited number of attempts to win!

## Table of Contents
- [Description](#description)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Description

This project is a Python-based console game where the player has to guess a hidden word by suggesting one letter at a time. The player loses a life each time they guess incorrectly, and the game ends when either all the letters are correctly guessed or the player runs out of lives.

### Features:
- **Random Word Selection**: The game selects a random word from a predefined list.
- **Dynamic Word Display**: As you guess correctly, the word is displayed with correctly guessed letters revealed.
- **Lives**: The player has a limited number of lives, represented by an array of stages.
- **Hangman Animation**: Each incorrect guess results in a "stage" of a hanging stick figure, symbolizing the player's decreasing chances.

## How to Play

1. The game will display a series of underscores (`_`) corresponding to the number of letters in the hidden word.
2. Guess a letter by typing it and hitting **Enter**.
3. If the guessed letter is in the word, it will replace the underscores in the word.
4. If the guessed letter is not in the word, the player loses a life, and a part of the stick figure is drawn.
5. The game continues until either:
   - The player guesses all the letters of the word, or
   - The player runs out of lives.

If you guess the word correctly, you'll see a "You win!" message. If you lose all your lives, the game ends.

## Requirements

- Python 3.x or higher

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/hangman-game.git

2. Navigate into the directory:

   ```bash
   cd hangman-game

3. Ensure you have Python installed by running:

   ```bash
   python --version

4. Install any dependencies (though none are specified for this basic version).

5. Run the game:

   ```bash
   python hangman.py

## License

This project is licensed under the MIT License.
