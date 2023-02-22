
with open("./Input/Letters/starting_letters.txt") as file:
    letter_template = file.read()
with  open("./Input/Names/names_list.txt", "r+") as file:
    names = file.read().split("\n")
for name in names:
    final_letter = letter_template
    final_letter = final_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", "x") as file:
        file.write(final_letter)
