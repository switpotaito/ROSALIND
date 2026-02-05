#Counting Point Mutations
#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t)

with open("rosalind_hamm.txt", "r") as f:
  seq1 = f.readline()
  seq2 = f.readline()
count = 0
for i in range(len(seq1)):
  if seq1[i] != seq2[i]:
    count = count + 1

print(count)
