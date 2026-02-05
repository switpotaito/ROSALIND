#Finding a Motif in DNA
#Given: Two DNA strings s and t(each of length at most 1 kbp)
#Return: All locations of t as a substring of s

with open("rosalind_subs.txt", "r") as f:
  s1 = (f.readline()).strip()
  s2 = (f.readline()).strip()

location = []
for i in range(0, len(s1) - len(s2) + 1, 1):
  if (s2 == s1[i:i+len(s2)]):
    location.append(i+1)

print(*(location))
