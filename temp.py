acronym = input('What acronym you want to add?\n')
definition = input('What is the deinition?\n')
with open('Acronyms.txt','w') as file :
    file.write(acronym +'-'+ definition + '\n')