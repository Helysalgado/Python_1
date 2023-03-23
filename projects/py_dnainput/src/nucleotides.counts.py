import os

path = r"C:\Users\chomb\Documents\GitHub\Python_1\scripts"
os.chdir(path)

#Defining variables 
dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
start_codon = 'TAC'
stop_codon = 'ATT'

#Defining result variables
start = dna.find(start_codon)
stop = dna.find(stop_codon)

#Get exon
exon = dna[start:stop]

#print results
print('Target Sequence\n',dna,'\n')
print('Exon begins at position:\t',start)
print('Exon ends at position:\t',stop)
print("Exon's length is:\t", len(exon),'\n\n')

#NEW EXERCISE
dna2 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#Counting de occurences
a = dna2.count("A")
t = dna2.count("T")
g = dna2.count("G")
c = dna2.count("C")

#Printing counts
print('Target Sequence\n',dna2,'\n')
print('Amount of Adenine:\t',a)
print('Amount of Thymine:\t',t)
print('Amount of Guanine:\t',g)
print('Amount of Cytosine:\t',c)

#INTERACTIVE
flag = 1
while flag == True:
    print('\nInput the target sequence to analyse')
    dna3 = input()

    #Counting de occurences
    a = dna3.count("A")
    t = dna3.count("T")
    g = dna3.count("G")
    c = dna3.count("C")

    #Printing counts
    print('\nTarget Sequence\n',dna3,'\n')
    print('Amount of Adenine:\t',a)
    print('Amount of Thymine:\t',t)
    print('Amount of Guanine:\t',g)
    print('Amount of Cytosine:\t',c)

    #Repeat
    print('\nDo you want to analyse another sequence?\n')
    print('\t\tYES[1]\tNO[0]')
    flag = input()

print("\n\t\tPROGRAM TERMINATED\n")