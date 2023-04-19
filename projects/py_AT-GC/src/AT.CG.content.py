## ---------------------------
##
## Script name: AT.GC.content 
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
## Notes: This script outputs the percentage of AT and GC content from file 'dna.txt' which is in 'data/' folder inside this project.
##
## IMPORTANT: It first sets the work directory to the path where 'dna.txt' is found. Change it to own directory so it functions. User can download 'dna.txt' form 'data/' folder inside this project.
##
## ---------------------------

import os

#Obtaining the directory where de file is found
print('Enter the path where the target file is located:')
path = input().rstrip("\n")
os.chdir(path)
print('\nYou are currently working on: ',os.getcwd(),'\n***"dna.txt" is found in here***\n')

print('Enter the input file:')
file = input().rstrip("\n")

#Opening the file and reading it
f = open(file, "r")
f = f.read()

#Counting the amount of nucleotides
print(f'File content:\n{f}\n')
a = f.count("A")
t = f.count("T")
g = f.count("G")
c = f.count("C")

#Calculating the percentages of AT and GC
per_at = round((a + t)/len(f)*100,2)
per_gc = round((g + c)/len(f)*100,2)

print('The percentages of AT and GC are the following')
print('%AT = ',per_at,'%')
print("%GC = ",per_gc,'%')

