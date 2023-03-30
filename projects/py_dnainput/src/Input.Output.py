import os
os.chdir(r"c:\Users\chomb\Documents\GitHub\Python_1\projects\py_dnainput\data")

#Defining variables
#Opens the file 'dna.txt'
ip_file = open(r"dna.txt")

#Reads the file and cuts the \n silent character
ip_read = ip_file.read().rstrip("\n")

#Creating the file '.fna' and overwriting it with what it is inside the original file
with open("dna.fna", "w") as file:
    file.write(ip_read)
    
print("\nNEW FILE CREATED\n")
       