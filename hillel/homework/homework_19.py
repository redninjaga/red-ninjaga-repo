# Author: Maksim Derevianko
import string

# 1
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}


def morse_code(text: str) -> str:
    text = text.upper()
    morse_text = ''
    for char in list(text):
        if char not in MORSE_CODE_DICT:
            return f"Error. Wrong user input. Dictionary doesn't have symbol: '{char}'"
        morse_text += MORSE_CODE_DICT.get(char) + ' '
    return morse_text


print(morse_code('Lera'))
