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

import os,re

#Function to obtain the directory and checking if it is empty or not 
def location():
    print('Enter the path where the target file is located:')
    path = input().rstrip("\n")
    os.chdir(path)
    directory = os.getcwd()
    print(f'\nYou are currently working on:\n\t{os.getcwd()}\n')

    #Checking directory content
    contents = os.listdir(directory)
    if contents:
        print(f'Directory content:')
        print(*contents, sep = "\n")
    else:
        print('\n\tERROR! EMPTY DIRECTORY\n\tQuiting program...\n')
        exit()

#Obteining the input file
def validating_file():
    try:
        print('\nEnter the input file:')
        file = input().rstrip("\n")
        print('\nValidating file...')

        #Checking if file is not empty
        if os.stat(file).st_size > 0:
            print('File verified successfuly.Exists')
        else:
            print('\n\tERROR! EMPTY FILE\n\tQuiting program...\n')
            exit()
        
        #Validating file
        file = open(file).readlines()
        file = concat_file(file)
        valid_nt(file)

    except OSError:
        print('\n\tERROR! NON EXISTING FILE\n\tQuiting program...\n')
        exit()
    
    return file

#Function that concatenates lines inside the file
def concat_file(file):
    print('Reading file content...')
    concat = ''
    for line in file:
        concat += line
    concat = concat.replace("\n", "")
    
    return concat

#Function that checks if file only contains "A","T","G","c"
def valid_nt(file):
    print('Verifying file content...')
    if re.search(r"[^ATGC]",file):
        print('\n\tERROR! INVALID FILE CONTENT\n\tQuiting program...\n')
        exit()
    else:
        print('File content verified successfuly')

location()
f = validating_file()

#Counting the amount of nucleotides
print(f'\nFile content:\n{f}\n')
a = f.count("A")
t = f.count("T")
g = f.count("G")
c = f.count("C")

#Calculating the percentages of AT and GC
per_at = round((a + t)/len(f)*100,2)
per_gc = round((g + c)/len(f)*100,2)

print('The percentages of AT and GC are the following')
print('%AT = ',per_at,'%')
print("%GC = ",per_gc,'%\n')

