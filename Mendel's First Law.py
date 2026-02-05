#Mendel's First Law
#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
#k individuals are homozygous dominant for a factor, m are heterozygous, and nare homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
#(and thus displaying the dominant phenotype). Assume that any two organisms can mate.

def pos_domal(k,m,n):
  case1 = (m/(k+m+n))*((m-1)/(k+m+n-1))*1/4
  case2 = (m/(k+m+n))*((n)/(k+m+n-1))*1
  case3 = (n/(k+m+n))*((n-1)/(k+m+n-1))
  final_prob = 1-(case1+case2+case3)
  return final_prob
