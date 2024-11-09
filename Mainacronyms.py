def find_acronyms():
        look_up = str(input("What software accornym would you like to look up?\n"))
        found = False
        try:
            with open ('Acronyms.txt') as file:
                for line in file:
                    if look_up in line:
                        found = True
                        print(line)
                        break
        except FileNotFoundError as e:
            print('File Not Found')
            return
        if not found:
                    print('The acronyms is not listed')

def add_acronyms():
        acronym = input('What acronym you want to add?\n')
        definition = input('What is the deinition?\n')
        with open('Acronyms.txt','a') as file :
            file.write(acronym +'-'+ definition + '\n')

def main():
      choice = input('Do you want to find(F) or add(A) an acronym\n')
      if choice == 'F':
            find_acronyms()
      elif choice == 'A':
            add_acronyms()

main()
               