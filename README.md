
## Pokemon Word Raider game

Pokémon Word Raider is a desktop guessing game where players try to guess the name of a randomly selected Pokémon character

Update on progress:

As it stands I currently have the game running in the terminal. Main game functions by using a while loop to return guesses and importing the random module from python.

Now have updated the script from a function to an object.



Wish List:

I would like to include in the future sound effects, background music, and a graphical splash and win screen but this can be worked on. I have some notes below on how I can implement. So far when I have attempting creating the exe file and then add images, it corrupts into a pyc file I cant debug. I also can't seem to decompile the files, or really know where to start. So my plan at the minute is to redo from the start and document as I got and push to a github repository so I can trace back my work. 


# Rescources

*Inspiration for the game basis and structure*
[Dataquest](https://app.dataquest.io/m/855/guided-project%3A-word-raider/2/creating-the-word-bank)

*Archive found to download Pokemon Sounds*
[Archive.org](https://archive.org/details/PokemonThemeSong)

*Convert MP3 files to Wav files* 
[Freeconvert.com](https://www.freeconvert.com/mp3-to-wav)

*General Pokemon Imagines downloaded from google images and converted to PNG files*

# Features

Background music during gameplay

Sound effects for winning and losing

Attempts-limited word guessing mechanic

Splash screen and Pokémon image when you win

GUI elements using tkinter

Random Pokémon selection each round


## Folder Structure

Pokemon Word Raider/
├── pokemon_word_raider.py

├── background_music.mp3

├── success.wav

├── fail.wav

├── pikachu.png

├── splash_logo.png (optional)

├── pokemon.ico (optional, for .exe icon)



## Requirements

Install these Python libraries before running the game:
```
pip install playsound pygame
```
No need to install pydub or ffmpeg since .wav files are used directly.


## How to Run

Open a terminal in the game folder.

Run the script using:

```
python pokemon word raider.py
```

##  Creating a Windows Executable (.exe)

Install PyInstaller:
```
pip install pyinstaller
```
Run the following command in the game folder:
```
pyinstaller --onefile --windowed --icon=pokemon.ico pokemon_word_raider.py
```
The .exe file will appear in the dist/ folder.



## Notes
All media files (music, images, sounds) must be in the same folder as the .py file or bundled with the .exe.

The splash screen image (splash_logo.png) is optional. If it’s not found, the game will display a simple title instead.

Ensure .wav and .mp3 files are valid and not corrupted.
