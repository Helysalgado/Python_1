import os

#Obtaining the directory where de file is found
os.chdir(r"C:\Users\chomb\Documents\GitHub\Python_1\projects\loops\data")
print(os.getcwd())
print('\nYou are currently working on: ',os.getcwd(),'\n***"4_input_adapters.txt" is found in here***\n')

print('Enter the input file:')
file = input().strip("\n")
print(file,'\n')

#Opening the file and reading line per line 
f = open(file, "r")
f = f.readlines()

#Using a loop for printing every line and removbign the special character '\n' in it
with open("4_input_adapters.fna", "w") as file:
    for line in f:
      line = line[:14] + '\n'
      file.write(str(line))