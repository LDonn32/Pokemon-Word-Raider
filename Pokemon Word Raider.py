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
    POKEMON_LIST = [
        "pikachu", "bulbasaur", "charmander", "squirtle", "jigglypuff",
        "meowth", "psyduck", "snorlax", "eevee", "mewtwo",
        "gengar", "lapras", "dragonite", "magikarp", "gyarados",
        "machamp", "alakazam", "pidgeotto", "rattata", "sandshrew",
        "vulpix", "growlithe", "abra", "kadabra", "bellsprout",
        "tentacool", "geodude", "ponyta", "slowpoke", "magnemite"
    ]

    def __init__(self):
        self.word = random.choice(self.POKEMON_LIST)
        self.guessed_letters = set()
        self.attempts = 6  # Default, updated in choose_difficulty
        self.difficulty = "medium"

    # Method to choose difficulty level
    # This method allows the player to choose a difficulty level which affects the number of attempts.
    def choose_difficulty(self):
        print("Choose a difficulty: easy / medium / hard")
        choice = input("Your choice: ").lower()
        
        # Set attempts based on difficulty choice using if-elif-else statements.
        # See: https://docs.python.org/3/tutorial/controlflow.html#if-elif-else
        if choice == "easy":
            self.attempts = 8
            self.difficulty = "easy"
        elif choice == "hard":
            self.attempts = 4
            self.difficulty = "hard"
        else:
            self.attempts = 6
            self.difficulty = "medium"

        # Print the difficulty level and attempts
        # Using f-strings for formatted output.
        # Using .capitalize() to format the difficulty level as a capitalized string.
        print(f"\nDifficulty set to {self.difficulty.capitalize()}. You have {self.attempts} attempts.\n")

    # Method to display the current state of the word
    # This method returns the word with guessed letters revealed and unguessed letters as underscores.
    # Gives the user a visual representation of their progress.
    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def play(self):
        print("Welcome to Pokemon Word Raider!")
        self.choose_difficulty()
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
                    print("\n🎉 Congratulations! You guessed the word:", self.word)
                    break
            else:
                print("Wrong guess.")
                self.attempts -= 1
        else:
            print("\n💀 Game over! The word was:", self.word)

# Main guard
if __name__ == "__main__":
    game = PokemonWordRaider()
    game.play()
