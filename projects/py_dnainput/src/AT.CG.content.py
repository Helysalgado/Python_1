import os

#Obtaining the directory where de file is found
os.chdir(r"C:\Users\chomb\Documents\GitHub\Python_1\projects\py_dnainput\data")
print(os.getcwd())
print('\nYou are currently working on: ',os.getcwd(),'\n***"dna.txt" is found in here***\n')

print('Enter the input file:')
file = input().rstrip("\n")

#Opening the file and reading it
f = open(file, "r")
f = f.read()

#Counting the amount of nucleotides
print('File content:\n',f)
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

