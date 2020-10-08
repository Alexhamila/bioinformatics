import sys

def main():
    '''Asks for a dna sequence and transcribes it.'''
    dna_sequence = input("Please, enter a DNA sequence: ")
    rna_sequence = ""
    valid_nucleotide = set("ACGT")

    for nucleotide in dna_sequence:
        if nucleotide not in valid_nucleotide:
            print(nucleotide, " is not a valid nucleotide.")
            sys.exit()
        if nucleotide == "T":
            rna_sequence = rna_sequence + "U"
        else:
            rna_sequence = rna_sequence + nucleotide
    print(rna_sequence)

main()
