DISCLAIMERS:
-DO NOT PIRATE GAMES
-THIS DOES PRESS KEYS ON YOUR KEYBOARD, BE WARNED
OF POTENTIAL MISHAPS DUE TO THIS
-THIS DOES READ YOUR KEYBOARD, BUT ONLY THE ESC
KEY
-----------------------------------------------------------

Dependancies:
-Windows OS (just what I'm using, can work with
linux or Mac with minor installation differences)

-Python 3.13 (what I used, latest should be fine)
https://www.python.org/downloads/

-pynput library
python -m pip install pynput

-mGBA (my choice of GBA emulator)
https://mgba.io

-Pokemon Ruby .gba file
Dump your own game

-----------------------------------------------------------

Tutorial:
-Put config.ini in C:\Users\"YourUser"\AppData\Roaming\mGBA
-Open mGBA and load your dumped game file
-Open KeyboardSTART.py to run the randomizer
-Press esc to end the randomizer
-Be sure to have the mGBA window focused

-----------------------------------------------------------

Functionality:
-Default settings
Every second a random number between 0 and 16 is generated.
#Movement
The w key is bound to Up and is called at 0, 7, or 13
The a key is bound to Left and is called at 1, 8, or 14
The s key is bound to Down and is called at 2, 9, or 15
The d key is bound to Right and is called at 3, 10, or 16
#Yes/No
The z key is bound to B and is called at 4 or 11
The x key is bound to A and is called at 5 or 12
#Start
The e key is bound to Start and is called at 6
#Savestate
The c key is bound to Save recent and is called every hour

-----------------------------------------------------------

Modifications:
-time.sleep is a timer with a numerical parameter
the number is in seconds
-Save state interval is also in seconds
-To change the stop key, change Key.esc to Key."Your_KEY"
-To change rates of key occurances, you can modify the
numbers in the "[]" characters, seperating each number
with ","
-If you want more or less generated numbers you can change
the range in the "()" characters in the random.randint
-Adding keys to the randomizer put the following in the
elif chain above "keyboard.press(key)"

elif number in ["Insert your numbers here"]:
            key = '"Your_Key"'