

with open("./Input/Names/invited_names.txt", mode="r") as f:
    names = f.readlines()

print(names)

clear_names = []
for name in names[:-1]:
    clear_names.append(name[:-1])
clear_names.append(names[-1])

print(clear_names)

with open("./Input/Letters/starting_letter.txt") as f:
    template = f.read()

print(template)

for name in clear_names:
    letter = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as f:
        f.write(letter)

