# n File Not Found error
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["keynotexist"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w") # check if there were a file, if not, create it
#     file.write("Something")
# except KeyError as error_message:
#     print(f"key:{error_message} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed.")
#     raise TypeError("That's the error that I made up.")
#
#
# height = float(input("Height:"))
# weight = int(input("Weight:"))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {value.letter: value.code for (key, value) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()
flag = 0
while flag == 0:
    try:
        answer = [phonetic[c] for c in name]
    except KeyError:
        print("Input can only be letter.")
        name = input("Enter your name:").upper()
    else:
        flag = 1

print(answer)




