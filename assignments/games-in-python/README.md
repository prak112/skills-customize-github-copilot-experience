
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and user input handling in Python.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create an interactive command-line Hangman game. The program should randomly choose a secret word from a predefined list, prompt the player to guess letters, and reveal progress until the player either guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Prompt the player for single-letter guesses and validate input.
- Display the current word progress using underscores for unknown letters (e.g. _ o _ _).
- Track and display letters already guessed (correct and incorrect).
- Limit the number of incorrect attempts and show remaining attempts.
- End the game with a clear win or lose message and reveal the secret word when the player loses.

#### Example session
```
Secret word: python
Progress: _ _ _ _ _ _
Guess: p
Progress: p _ _ _ _ _
Guess: x
Incorrect guesses remaining: 5
...
You win! The word was: python
```

**Skills practiced:** String manipulation, loops, conditionals, randomness, and user I/O
