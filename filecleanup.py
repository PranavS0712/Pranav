import os
#os.mkdir(r"C:\Users\I513656\OneDrive - SAP SE\BDC Learning\Python\cleanup")

folder = r'C:\Users\I513656\OneDrive - SAP SE\BDC Learning\Python'
entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)

