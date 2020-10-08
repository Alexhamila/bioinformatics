# Author: Alexandre Hamila
# Date: 9/16/2020
#
# This program identifies the longest 
# ORF between 3 => 5'-3' and 3'5' strands
# if it exists.
# Within a sequence obtained inside a .txt file

def antisens(sequence):
    '''  Converts nucleotides from a 5-3 strand to a 3-5 strand.
              Complementarity A <=> T and C <=> G
            Accepts as parameter a sequence in str       '''

    sequence_antisens = ''
    for nucleotide in sequence:
        if nucleotide == 'A':
            sequence_antisens = sequence_antisens + 'T'
        elif nucleotide == 'T':
            sequence_antisens = sequence_antisens + 'A'
        elif nucleotide == 'G':
            sequence_antisens = sequence_antisens + 'C'
        elif nucleotide == 'C':
            sequence_antisens = sequence_antisens + 'G'
    return sequence_antisens

def readFile(path):
    ''' Reads file.txt '''
    sequence_file = open(path)  # we retrieve file.txt

    # we retrieve the sequence from the file and convert the sequence
    # in uppercase to avoid a dna sequence of type: AcTgaA
    full_sequence = sequence_file.read().upper().strip()

    sequence_file.close()       # close the .txt file
    return full_sequence

def convertTroisChar(sequence):
    ''' Retourne la séquence séparé en une liste de 3 charactere '''
    return [sequence[i:i + 3] for i in range(0, len(sequence), 3)]


cstart = "ATG"                 # start codon
cstop = ["TAA", "TAG", "TGA"]  # stop codon

# file name .txt
sequence_path = input("Adress of file (ex: orf_sequence_1.txt): ")

full_sequence = readFile(sequence_path)

# sequence frame 1 | 2 | 3
sequence_cadre1 = full_sequence
sequence_cadre2 = full_sequence[1:]
sequence_cadre3 = full_sequence[2:]

# frame 1 | 2 | 3 in list of 3 chars
sequence_cadre1 = convertTroisChar(sequence_cadre1)
sequence_cadre2 = convertTroisChar(sequence_cadre2)
sequence_cadre3 = convertTroisChar(sequence_cadre3)

#full_sequence but inverse and complementary
full_sequence_reversed = antisens(full_sequence[::-1])

# inversion of the sequence: frame -1 | -2 | -3
sequence_reversed1 = full_sequence_reversed
sequence_reversed2 = full_sequence_reversed[1:]
sequence_reversed3 = full_sequence_reversed[2:]

sequence_reversed1 = convertTroisChar(sequence_reversed1)
sequence_reversed2 = convertTroisChar(sequence_reversed2)
sequence_reversed3 = convertTroisChar(sequence_reversed3)

# list containing the 6 frames
sequences = [sequence_cadre1, sequence_cadre2, sequence_cadre3, sequence_reversed1, sequence_reversed2, sequence_reversed3]

# dic of the start codon indexes for each frame
cstart_index = {}

# dico des index des 3 codons stop pour chaque cadre
cstop_index = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5:{}}


# dic of the indexes of the 3 stop codons for each frame
for i in range(0,6):
    """ We try to find a start codon in each of the 6 frames """.
    """ If there is a start codon then we save the index for this frame """"".
    """ Otherwise we define the string none in the start index dictionary for this frame """.
    try:
        cstart_index[i] = sequences[i].index(cstart)
    except ValueError:
        cstart_index[i] = "none"

for i in range(0,6):
    """We try to find one, two or three stop codons in each of the 6 frames."""
    """ and take the highest index of the three """.

    # highest index temporary variable between the 3 stop codons
    cstop_index_highest = "none"
    for i_cstop in range(0,3):
        try:
            cstop_index_current = sequences[i].index(cstop[i_cstop])
           # if the discovered index is greater than our temporary variable (or if the temporary variable is empty)
            if cstop_index_highest == "none" or cstop_index_highest < cstop_index_current:
                # we define our temporary variable as the discovered index
                cstop_index_highest = cstop_index_current
        except ValueError:
            pass

     # we add, if necessary, our largest stop codon in the stop codon dic to its number frame i
    cstop_index[i] = cstop_index_highest

# dic which will take the difference between the start and stop codon indexes for each frame
orf_length = {}
# dic which will take the value of a sub_dic for each frame with in 0: the index cstart and in 1: the index cstop
orf_values = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}}

for i in range(0,6):
    if cstart_index[i] != "none" and cstop_index[i] != "none" and cstart_index[i] < cstop_index[i] :
        orf_length[i] = cstop_index[i] - cstart_index[i]
        orf_values[i][0] = cstart_index[i]
        orf_values[i][1] = cstop_index[i]
    else:
        pass

max_length = 0
key = "none"

for i in orf_length:
    if orf_length[i] > max_length:
        max_length = orf_length[i]
        key = i

if max_length > 0:
    if key < 3:
        print("Sequence:", full_sequence[(orf_values[key][0] * 3 + key):(orf_values[key][1]*3 + key)])
        print("Length of ORF:", str(max_length * 3))
        print("Value of STOP:", full_sequence[(orf_values[key][1]*3 + key):(orf_values[key][1]*3+3+key)])
        print("Frame 5'-3': " +str(key+1))
    else:
        print("Sequence:", full_sequence_reversed[(orf_values[key][0] * 3 + (key-3)):(orf_values[key][1]*3 + (key-3))])
        print("Length of ORF:", str(max_length * 3))
        print("Value of STOP:", full_sequence_reversed[(orf_values[key][1]*3 + (key-3)):(orf_values[key][1]*3+3+(key-3))])
        print("Frame 3'-5': -" +str(key-2))
else:
    print("No ORF detected in this sequence")