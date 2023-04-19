## ---------------------------
##
## Script name: class.nucleotides.counts
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
## Notes: This script outputs the start codon position, stop codon position, exon sequence and the amount of A's, T's, C's and G's inside the exon. Target sequence is provided in a message before user inputs sequence.
##
## IMPORTANT: No complementary files. Sequence is provided and user inputs it. 
##
## ---------------------------

#Defining dna class
class dna():
    #Variables all set and initialized 
    start_codon = 'TAC'
    stop_codon = 'ATT'
    pos_start = 0
    pos_stop = 0
    length = 0
    exon = ''
    a = 0
    t = 0
    g = 0
    c = 0

    #Constructor that requires the sequence parameter
    def __init__(self, x = ''):
        self.sequence = x
    
    #Method that returns the postition of the start codon
    def posstart(self):
        self.pos_start = self.sequence.find(self.start_codon)
        return self.pos_start

    #Method that returns the postition of the stop codon
    def posstop(self):
        self.pos_stop = self.sequence.find(self.stop_codon)
        return self.pos_stop
    
    #Method that returns the length of exon and its sequence
    def exonlength(self):
        #Slicing the sequence according to start and end of the exon
        self.exon = self.sequence[self.pos_start:self.pos_stop+3]

        #Obtaining the length of the exon obtained 
        self.length = len(self.exon)
        return self.length

    #Method that counts each nucleotide in the exon
    def ntamount(self):
        self.a = self.exon.count("A")
        self.t = self.exon.count("T")
        self.g = self.exon.count("G")
        self.c = self.exon.count("C")
    
    #Method that casts the variable 'exon' to a string, not to a memory direction
    def __str__(self):
        self.string = self.exon
        return self.string

#MAIN
print('INPUT THE SEQUENCE UP TO ANALYSE')
print('SUGESTED Target sequence:\tAAGGTACGTCGCGCGTTATTAGCCTAAT')
x = dna(input().rstrip("\n"))

#Applying all the methods to 'x' variable
x.posstart()
x.posstop()
x.exonlength()
x.ntamount()
x.__str__()

#Print all variables needed
print('Target Sequence\n',x.string)
print('\n>Exon begins at position:\t',x.pos_start)
print('>Exon ends at position:\t\t',x.pos_stop)
print(">Exon's sequence is:\t\t",x.exon)
print(">Exon's length is:\t\t",x.length)
print('>Amount of Adenine:\t\t',x.a)
print('>Amount of Thymine:\t\t',x.t)
print('>Amount of Guanine:\t\t',x.g)
print('>Amount of Cytosine:\t\t',x.c)