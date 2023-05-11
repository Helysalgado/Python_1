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

#Function that creates new file
def creating_file(file):
    #Creating the file '.fna' and overwriting it with what it is inside the original file
    print('\nEnter the new file name:')
    newname = input().rstrip("\n")
    with open(newname, "w") as file:
        file.write(ip_read)
        
    print("\n\tNEW FILE CREATED\n")

#MAIN
location()
ip_read = validating_file()
creating_file(ip_read)