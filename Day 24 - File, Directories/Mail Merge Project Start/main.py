# TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as letter_tem:
    contents = letter_tem.read()
    with open("Input/Names/invited_names.txt") as names:
        for i in range(1, 9):
            name = names.readline()
            name = name.strip("\n")
            letter = contents.replace("[name]", f"{name}")
            with open(f"Output/ReadyToSend/{name}_invitation", "w") as new_letter:
                new_letter.write(f"{letter}")


# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
