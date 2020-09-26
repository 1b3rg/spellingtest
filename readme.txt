26-Sep-2020
Nathan Vandenberg

This script, written in Python, executes a spelling test.

The user can enter any number of words to be tested.
The words are stored in a List and can also be saved to a text file
in the same directory as the Python script.
The next time the user runs the script they can import a list of words
from the text file.

The script asks the user to spell each word one after the other.
The script shows each word briefly and also uses the Google text-to-speech
API gTTS to speak the word.
The user must spell each word correctly before they can continue to the
next word.
After two wrong attempts the user is shown the word again and the word is
also spoken again.

The user is also shown their progress as a % complete.
Once complete the user can choose to spell the list again or finish.

