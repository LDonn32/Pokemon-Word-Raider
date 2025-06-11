# pokemon_game.py
# Author: Laura Donnelly	

# This is the object of the Pokemon Word Raider game.
# Adding the code here to import it as an object in the future.
# This will allow for debugging and testing the game more easily.


import random

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
        self.attempts = 6
        self.difficulty = "medium"

    def choose_difficulty(self):
        print("Choose a difficulty: easy / medium / hard")
        choice = input("Your choice: ").lower()

        if choice == "easy":
            self.attempts = 8
            self.difficulty = "easy"
        elif choice == "hard":
            self.attempts = 4
            self.difficulty = "hard"
        else:
            self.attempts = 6
            self.difficulty = "medium"

        print(f"\nDifficulty set to {self.difficulty.capitalize()}. You have {self.attempts} attempts.\n")

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
