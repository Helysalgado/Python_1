## ---------------------------
##
## Script name: Input.Output
##
##
## Author: Bernardo Chombo Álvarez
##
## Date Created: 2023-03-30
##
## Copyright (c) Bernardo, Chombo-Álvarez 2023
## Email: bchombo@lcg.unam.mx
##
## ---------------------------
##
## Notes: This script outputs a fasta file from a DNA sequence found in 'dna.txt' file which is found in 'data/' folder inside this project.
##
## IMPORTANT: It first sets the work directory to the path where 'dna.txt' is found. Change it to own directory so it functions. User can download 'dna.txt' form 'data/' folder inside this project.
##
## ---------------------------

import os
os.chdir(r"c:\Users\chomb\Documents\GitHub\Python_1\projects\py_dnainput\data")

#Defining variables
#Opens the file 'dna.txt'
print('Enter de input file:')
f = input().rstrip("\n")
ip_file = open(f)

#Reads the file and cuts the \n silent character
ip_read = ip_file.read().rstrip("\n")

#Creating the file '.fna' and overwriting it with what it is inside the original file
print('Enter the new file name:')
newname = input().rstrip("\n")
with open(newname, "w") as file:
    file.write(ip_read)
    
print("\nNEW FILE CREATED\n")
       