# Gives string, print the corresponding letter for each letter in string. ACTG --> TGAC
def DNA(dna):
	dna = dna.lower()
	out = ""
	for i in dna:
		if i == 'a':
			out += 'T'
		elif i == 't':
			out += 'A'
		elif i == 'c':
			out += 'G'
		elif i == 'g':
			out += 'C'
	return out

print(DNA('ACTG'))