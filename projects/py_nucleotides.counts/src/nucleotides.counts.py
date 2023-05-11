## ---------------------------
##
## Script name: nucleotides.counts
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
## Notes: This script outputs the amount of A's, T's, C's and G's inside a sequence that user inputs.
##
## IMPORTANT: No complementary files. User inputs the sequence. 
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


#MAIN
flag = True
while flag:
    location()
    dna = validating_file()

    #Counting de occurences
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    #Printing counts
    print('\nTarget Sequence\n',dna,'\n')
    print('Amount of Adenine:\t',a)
    print('Amount of Thymine:\t',t)
    print('Amount of Guanine:\t',g)
    print('Amount of Cytosine:\t',c)

    #Repeat
    print('\nDo you want to analyse another sequence?\n')
    print('\t\tYES[1]\tNO[0]')

    #Casting the input so loop can continue or stop
    flag = int(input().rstrip("\n"))

print("\n\t\tPROGRAM TERMINATED\n")
