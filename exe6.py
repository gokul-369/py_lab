import os
file = input("Enter directory path: ")#E://folder//filename.extension
 
num_words = 0
 
with open(file, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("\n Number of words:")
print(num_words)
