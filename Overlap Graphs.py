#Overlap Graphs

result = []
with open("rosalind_grph.txt", "r") as f:
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

ids = list(sequences.keys())

for id1 in ids:
    for id2 in ids:
        if id1 == id2:
            continue
        seq1 = sequences[id1]
        seq2 = sequences[id2]
        
        if seq1[-3:] == seq2[:3]:
            print(f"{id1} {id2}")
