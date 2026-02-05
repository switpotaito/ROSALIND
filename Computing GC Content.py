#Computing GC Content
#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 

result = []
with open("rosalind_gc.txt", "r") as f:
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

seq_itself = list(sequences.values())
for i in range(len(seq_itself)):
  GC_count = seq_itself[i].count("G") + seq_itself[i].count("C")
  GC_content = (GC_count / len(seq_itself[i])) * 100
  seq_itself[i]= GC_content

seq_name = list(sequences.keys())
for i in range(len(seq_itself)):
  sequences[seq_name[i]] = seq_itself[i]

max_value = max(seq_itself)
for key, value in sequences.items():
  if value == max_value:
    print(key)
    print(value)
