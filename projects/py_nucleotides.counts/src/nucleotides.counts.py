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

#INTERACTIVE
#Using a variable set true for while loop
flag = True
while flag:
    print('\nInput the target sequence to analyse')
    dna = input().rstrip("\n")

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
