from morse_converter import *

keep_going = True
# Ask the user if they want to convert a text?

while keep_going:
    start = input("Wanna send some secrets? (Y/N) ").upper()
    if start == "N":
        keep_going = False
        print("Mission Completed")
    elif start == "Y":
        print("Good .. ")
        text = input("What is your secret ?? ").upper()
        code = to_morse(text)
        print(f"Your Secret is now {code}")

        # Ask if they want to decipher the message back
        decode = input("Incase you forgot your message, Wanna decipher it back? (Y/N) ").upper()
        if decode == "Y":
            print(f"Okay then, your message {code} was {from_morse(code)}")
        elif decode == "N":
            pass
        else:
            print("I do not understand you .. ")
    else:
        print("I do not understand .. ")
