#Consensus and Profile
#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.

result = []
with open("rosalind_cons.txt", "r") as f:
  for line in f:
    result.append(line.strip())

sequences = {}
current_id = ""

for item in result:
    if item.startswith(">"):
        current_id = item[1:]
        sequences[current_id] = "" 
    else:
      if current_id:
        sequences[current_id] += item 

seq = list(sequences.values())
matrix = [list(s) for s in seq]

def count_base(seq_list, matrix, base):
  list1 = []
  for i in range(len(seq_list[0])):
    count = 0
    for j in range(len(seq_list)):
      if matrix[j][i] == base:
        count += 1
    list1.append(count)
  return list1

countA_list = count_base(seq, matrix, "A")
countC_list = count_base(seq, matrix, "C")
countG_list = count_base(seq, matrix, "G")
countT_list = count_base(seq, matrix, "T")

count_matrix = [countA_list, countC_list, countG_list, countT_list]

consen_seq = ""
for i in range(len(countA_list)):
    max = 0
    for j in range(4):
      if count_matrix[j][i] > max:
        max = count_matrix[j][i]
        index = j
    if index == 0:
      consen_seq += "A"
    elif index == 1:
      consen_seq += "C"
    elif index == 2:
      consen_seq += "G"
    elif index == 3:
      consen_seq += "T"

profile = {
    "A": countA_list,
    "C": countC_list,
    "G": countG_list,
    "T": countT_list}

print(consen_seq)
for nt in ["A", "C", "G", "T"]:
    print(f"{nt}:", *(profile[nt]))
