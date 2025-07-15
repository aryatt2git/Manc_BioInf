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

def reverse_comp(sequence):

    rev_comp_seq = ''

    reverse_seq = sequence[::-1].lower().replace(' ', '')

    for nucleotide in reverse_seq:

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

#reverse_comp(sequence)

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

        rev_prot_seq = reverse_comp(sequence)[i:len(sequence)]

        reverses.append(DNA2Prot(rev_prot_seq))

    print('Forward')
    for seq in forwards:
        print(seq)

    print('Reverse')
    for seq in reverses:
        print(seq)

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

def nucleotide_count(sequence, number):

    from itertools import product

    nucleotides = ['a', 'c', 'g', 't']

    combinations = [''.join(combination) for combination in product(nucleotides, repeat = number)]

    nucleotide_dict = {}

    for comb in combinations:

        nucleotide_dict[comb] = 0

    for nn in range(0, len(sequence)+number, number):

        xx = sequence[nn - number:nn]

        if xx in nucleotide_dict.keys():

            nucleotide_dict[xx] = nucleotide_dict[xx] + 1

    for item in nucleotide_dict:
        if nucleotide_dict[item] > 0:
            print(item, ': ', nucleotide_dict[item])

sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
nucleotide_count(sequence, 3)