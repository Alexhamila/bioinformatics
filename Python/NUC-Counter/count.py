
import sys

def main():
    """Check count of each nucleotide"""
    dna_sequence = input("Please, enter a DNA sequence: ").upper()
    #Valid accepted nucleotides
    valid_nucleotides = set("ATCG")
    #Initial count of nucleotides
    count = {"A": 0, "T": 0, "C": 0, "G": 0}


    #For each nucleotide in dna sequence
    for nucleotide in dna_sequence:
        #If nucleotide is not A, T, C or G
        if nucleotide not in valid_nucleotides:
            print(nucleotide, "is not a valid nucleotide.")
            sys.exit()
        else:
            count[nucleotide] = count[nucleotide]+1

    for nucleotide, value in count.items():
        print("Number of", nucleotide, "is", value)

main()