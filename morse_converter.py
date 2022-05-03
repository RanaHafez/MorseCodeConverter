from constants import MORSE_CODE


def to_morse(message):
    cipher = ""
    for char in message:
        if char.isalpha():
            cipher += MORSE_CODE[char]
            cipher += "/"
        else:
            cipher += char
    return cipher


def get_letter(ciphered_letter):
    for letter, cipher in MORSE_CODE.items():
        if ciphered_letter == cipher:
            return letter


def from_morse(cipher_text):
    words = cipher_text.split("/")[:-1]
    ans = ""
    for word in words:
        if " " in word:
            ans += " "
            word = word.strip()
        ans += get_letter(word)
    return ans


