# Pokemon Word Raider Game
# A simple word guessing game where players guess the names of Pokemon.

# Author: Laura Donnelly

# Plan on expanding the game with more features in the future.
# Such as adding pictures and sound affects, adding difficulty levels and exporting the game to a web app.

# Import necessary libraries
# Importing random to select a random Pokemon from the list.
# See: https://docs.python.org/3/library/random.html
import random


# List of Pokemon names to choose from
# This list can be expanded with more Pokemon names as needed.
# The names are in lowercase to ensure consistent comparison during the game.
POKEMON_LIST = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "jigglypuff",
    "meowth", "psyduck", "snorlax", "eevee", "mewtwo",
    "gengar", "lapras", "dragonite", "magikarp", "gyarados",
    "machamp", "alakazam", "pidgeotto", "rattata", "sandshrew",
    "vulpix", "growlithe", "abra", "kadabra", "bellsprout",
    "tentacool", "geodude", "ponyta", "slowpoke", "magnemite"
]

# Function to choose a random Pokemon word from the list
# This function returns a random Pokemon name in lowercase.
def choose_word():
    return random.choice(POKEMON_LIST).lower()

# Function to display the current state of the word being guessed
# This function takes the word and a set of guessed letters,
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
# This function handles the game logic, including user input and game flow.
# Giving users 6 goes to guess the word.
def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Pokemon Word Raider!")
    print("Guess the Pokemon name!")

    # While loop to continue the game until the user runs out of attempts or guesses the word
    # The loop will display the current state of the word, the guessed letters, and the number of attempts left.
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print("Wrong guess.")
            attempts -= 1
    else:
        print("\nGame over! The word was:", word)

# Using a main guard to run the game
# This allows the game to be run directly or imported without executing the game automatically.
# Using this for now until I expand the game with more features or export to exe file
if __name__ == "__main__":
    play_game()