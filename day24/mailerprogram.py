with open("day24/names.txt", "r") as f:
    names=f.readlines()
for i in range(len(names)):
    names[i]=names[i].strip()
with open("day24/start_letter.txt", "r") as f:
    letter_start=f.read()

# print(names)
# print(letter_start)
for name in names:
    letter=letter_start.replace("[name]", name)
    with open("day24/letters_to_send/Letter for "+name+".txt", "w") as f:
        f.write(letter)