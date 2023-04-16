## ---------------------------
##
## Script name: fasta.format
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

#Obtaining the directory where de file is found
os.chdir(r"C:\Users\chomb\Documents\GitHub\Python_1\projects\loops\data")
print(os.getcwd())
print('\nYou are currently working on: ',os.getcwd(),'\n***"dna_sequences.txt" is found in here***\n')

print('Enter the input file:')
file = input().strip("\n")
print(file,'\n')

#Opening the file and reading line per line 
f = open(file, "r")
f = f.readlines()

#Using a loop for printing every line and removing the special character '\n' in it
with open("dna_sequences.fna", "w") as file:
    for line in f:
        #Obtaining the sequence name
        name_seq = '> ' + line[:5]

        #Obtaining the sequence
        seq = line[8:]

        #Concatenating the output format
        output = name_seq + '\n' + seq
        file.write(str(output))