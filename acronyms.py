look_up = str(input("What software accornym would you like to look up?\n"))
found = False
with open ('Acronyms.txt') as file:
    for line in file:
        if look_up in line:
            found = True
            print(line)
            break
if not found:
            print('The acronyms is not listed')
           