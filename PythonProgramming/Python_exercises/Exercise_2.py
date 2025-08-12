# 2.1 Create a function to convert DNA string into fasta format

def convert2fasta(sequence):

    for rows in range(60, len(sequence) + 60, 60):

        row_sequence = sequence[rows-60:rows].lower()

        print(str(rows - 59).rjust(len( str( len(sequence) + 60 ))), end='\t')

        for fragments in range(10, len(row_sequence) + 10, 10):

            split_sequence = row_sequence[fragments-10:fragments]
            print(split_sequence, end=' ')

        print('')

sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG"

convert2fasta(sequence)

# 2.2 Convert DNA sequence into translated protein sequence

def DNA2Prot(sequence):

    DNA_sequence = sequence.upper().replace(' ', '')

    trans_seq = {}
    trans_seq['F'] = ['TTT', 'TTC']
    trans_seq['L'] = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
    trans_seq['I'] = ['ATT', 'ATC', 'ATA']
    trans_seq['M'] = ['ATG']
    trans_seq['V'] = ['GTT', 'GTC', 'GTA', 'GTG']
    trans_seq['S'] = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
    trans_seq['P'] = ['CCT', 'CCC', 'CCA', 'CCG']
    trans_seq['T'] = ['ACT', 'ACC', 'ACA', 'ACG']
    trans_seq['A'] = ['GCT', 'GCT', 'GCA', 'GCG']
    trans_seq['Y'] = ['TAT', 'TAC']
    trans_seq['*'] = ['TAA', 'TAG', 'TGA']
    trans_seq['H'] = ['CAT', 'CAC']
    trans_seq['Q'] = ['CAA', 'CAG']
    trans_seq['N'] = ['AAT', 'AAC']
    trans_seq['K'] = ['AAA', 'AAG']
    trans_seq['D'] = ['GAT', 'GAC']
    trans_seq['E'] = ['GAA', 'GAG']
    trans_seq['C'] = ['TGT', 'TGC']
    trans_seq['W'] = ['TGG']
    trans_seq['R'] = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
    trans_seq['G'] = ['GGT', 'GGC', 'GGA', 'GGG']

    protein_sequence = ''

    for position in range(3, len(DNA_sequence) + 3, 3):
        
        codon = DNA_sequence[position - 3 : position]

        for nucleotide in codon:
            if nucleotide not in ['A', 'C', 'G', 'T']:
                protein_sequence += '-codon not recognised-'

        for key, value in trans_seq.items():

            if codon in value:

                protein_sequence += key

        if len(codon) < 3:

            protein_sequence += '-end of sequence out of frame'

    print(protein_sequence)
    return protein_sequence

#sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
#sequence = 'ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA'

#DNA2Prot(sequence)

'''
Answer: MDLSALRVEEVQNVINAMQKILECPICLELIKEPVSTKCDHIFCKFCMLKLLNQKKGPSQCPLCKNDITK
'''

# 2.3 Write a function that generates the reverse compliment of a sequence

def reverse_seq(sequence):

    rev_comp_seq = ''

    reversed_seq = sequence[::-1].lower().replace(' ', '')

    for nucleotide in reversed_seq:

        if nucleotide == 'a':
            rev_comp_seq += 't'

        elif nucleotide == 't':
            rev_comp_seq += 'a'

        elif nucleotide == 'g':
            rev_comp_seq += 'c'

        elif nucleotide == 'c':
            rev_comp_seq += 'g'

        else:
            rev_comp_seq += 'N'

    print(rev_comp_seq)
    return rev_comp_seq

#sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
#sequence ='GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT'

#reverse_seq(sequence)

'''
Answer: atcaaatctcgtactttcttgtaggctccttttggttatatcattcttacataaaggacactg
        tgaaggccctttcttctggttgagaagtttcagcatgcaaaatttgcaaaatatgtggtcaca
        ctttgtggagacaggttccttgatcaactccagacagatgggacactctaagattttctgcat
        agcattaatgacattttgtacttcttcaacgcgaagagcagataaatccatttctttctgttc
        caatgaactttacccagagcagagggtgaaggcctcctgagcgcaggggcccagttatctgag
        aaaccccacagcctgtcccccgtccaggaagtctcagc
'''

# 2.4 Reverse compliment and translate a six frame translation of a DNA sequence

def six_frame_trans(sequence):

    forwards = []
    reverses = []

    for i in range(0, 3):

        input_seq = sequence[i:len(sequence)]

        forw_prot_seq = DNA2Prot(input_seq)

        forwards.append(forw_prot_seq)

        rev_prot_seq = reverse_seq(sequence)[i:len(sequence)]

        reverses.append(DNA2Prot(rev_prot_seq))

    print('Forward')
    for seq in forwards:
        print(seq)

    print('Reverse')
    for seq in reverses:
        print(seq)

    return forwards, reverses

# sequence_one = 'aggagtaagcccttgcaactggaaatacacccattg'
# six_frame_trans(sequence_one)

# sequence_two = 'GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCC'
# six_frame_trans(sequence_two)

'''
Answer:

Forward
AETSWTGDRLWGFSDNWPALRRPSP
LRLPGRGTGCGVSQITGPLRSGGLH-end of sequence out of frame
*DFLDGGQAVGFLR*LGPCAQEFT-end of sequence out of frame
Reverse
G*RPPERRGPVI*ETPQPVPRPGSLS
GEGLLSAGQLSEKPHSLSPVQEVS-end of sequence out of frame
VKS*AQGPSYLRNPTCPPSRKSQ-end of sequence out of frame
'''

# 2.5 Count single, di-nucleotide and tri-nucleotides in a sequence

from itertools import product

def nucleotide_count(sequence, number):

    nucleotides = ['A', 'C', 'G', 'T']

    combinations = [''.join(combination) for combination in product(nucleotides, repeat = number)]

    nucleotide_dict = {}

    for comb in combinations:

        nucleotide_dict[comb] = 0

    for nn in range(0, len(sequence)+number, number):

        xx = sequence[nn - number:nn].upper()

        if xx in nucleotide_dict.keys():

            nucleotide_dict[xx] = nucleotide_dict[xx] + 1

    for item in nucleotide_dict:
        if nucleotide_dict[item] > 0:
            print(f'{item}: {nucleotide_dict[item]}')

    return nucleotide_dict

sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
# sequence = 'GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA'
nucleotide_count(sequence, 3)

'''
Answer: 

A :  89
C :  58
G :  62
T :  71

AA :  18
AC :  9
AG :  8
AT :  11
CA :  6
CC :  9
CG :  1
CT :  7
GA :  15
GC :  4
GG :  9
GT :  5
TA :  4
TC :  13
TG :  11
TT :  10

AAA :  1
AAC :  1
AAG :  4
AAT :  2
ACA :  1
ACC :  4
ACG :  2
ACT :  3
AGA :  1
AGG :  2
AGT :  4
ATA :  1
ATC :  2
ATT :  1
CAA :  6
CAG :  2
CCC :  1
CCT :  3
CGG :  1
'''

# 2.6 Develop a function which gives the GC content of a sequence

def GC_content(sequence):

    nucleotide_count_dict = nucleotide_count(sequence, 1)

    GC_cont = ((nucleotide_count_dict['G'] + nucleotide_count_dict['C']) / len(sequence)) * 100

    GC_percent = '{:.2f}'.format(GC_cont)

    print(f'The GC content is {GC_percent}%    ')

# sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
sequence = 'GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA'

GC_content(sequence)

'''
Answer: The GC content is 42.86%
'''