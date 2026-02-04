#3. get reverse complement of a DNA string s
#when s is given DNA sequence, solution is written below.
s_reverse = s[::-1]
s_reverse = s_reverse.replace("A","X")
s_reverse = s_reverse.replace("T","A")
s_reverse = s_reverse.replace("X","T")
s_reverse = s_reverse.replace("C","Y")
s_reverse = s_reverse.replace("G","C")
s_reverse = s_reverse.replace("Y","G")
s_reverse
