# Pokemon Word Raider Game
# A simple word guessing game where players guess the names of Pokemon.

# Author: Laura Donnelly

# Plan on expanding the game with more features in the future.
# Such as adding pictures and sound affects, adding difficulty levels and exporting the game to a web app.

# Import necessary libraries
# Importing random to select a random Pokemon from the list.
# See: https://docs.python.org/3/library/random.html
import random

# Define the PokemonWordRaider class
# Using an object instead of a function to run the game. 
# Doing this allows for easier expansion in the future.

# This class contains the list of Pokemon, the game logic, and methods to display the word and handle guesses.
class PokemonWordRaider:
    # List of Pokemon names to guess
    # This list can be expanded with more Pokemon names as needed.
    POKEMON_LIST = [
        "pikachu", "bulbasaur", "charmander", "squirtle", "jigglypuff",
        "meowth", "psyduck", "snorlax", "eevee", "mewtwo",
        "gengar", "lapras", "dragonite", "magikarp", "gyarados",
        "machamp", "alakazam", "pidgeotto", "rattata", "sandshrew",
        "vulpix", "growlithe", "abra", "kadabra", "bellsprout",
        "tentacool", "geodude", "ponyta", "slowpoke", "magnemite"
    ]
    # Using init method to initialize the game state
    # This method sets a random Pokemon word, initializes guessed letters, and sets the number of attempts.
    # See: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    def __init__(self):
        self.word = random.choice(self.POKEMON_LIST)
        self.guessed_letters = set()
        self.attempts = 6

    # Method to display the current state of the word with guessed letters revealed
    # This method returns a string representation of the word with guessed letters shown and unguessed letters as underscores.
    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def play(self):
        print("Welcome to Pokemon Word Raider!")
        print("Guess the Pokemon name!")

        while self.attempts > 0:
            print("\nWord:", self.display_word())
            print("Guessed letters:", ' '.join(sorted(self.guessed_letters)))
            print(f"Attempts left: {self.attempts}")

            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                print("Good guess!")
                if all(letter in self.guessed_letters for letter in self.word):
                    print("\nCongratulations! You guessed the word:", self.word)
                    break
            else:
                print("Wrong guess.")
                self.attempts -= 1
        else:
            print("\nGame over! The word was:", self.word)

# Main guard
if __name__ == "__main__":
    game = PokemonWordRaider()
    game.play()
