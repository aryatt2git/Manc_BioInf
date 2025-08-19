import os
import re
from six_frame_trans import six_frame_trans as sft

filename = './U15422.1.fasta'

filepath = os.getcwd()

file = f'{filepath}/{filename}'

raw_fasta_sequence = ''

with open(file) as fasta_file:

    next(fasta_file)

    for lines in fasta_file:

        raw_fasta_sequence = raw_fasta_sequence + lines

    fasta_sequence = raw_fasta_sequence.replace('\n', '')

    ORF_sequences = []

    '''for seq in re.finditer(r'(?:ATG)((?:[ATGC])*?)(?:TAG|TAA|TGA)', fasta_sequence):

        ORF = seq.group(0)

        if len(ORF) > 3 and len(ORF) % 3 == 0:

            ORF_sequences.append(ORF)

    ORF_sequence = ''

    for sequence in ORF_sequences:

        if len(sequence) > len(ORF_sequence):

            ORF_sequence = sequence

    sft(ORF_sequence)'''

    for i in range(len(fasta_sequence)):

        ORF_sequences_TAG = re.findall('^ATG(([ACGT]+)*?)TAG', fasta_sequence[i:])

        for seq in ORF_sequences_TAG:

            if len(seq) > 1 and len(seq) % 3 == 0:

                ORF_sequences.append(seq)

        ORF_sequences_TGA = re.findall('^ATG[ACGT]+TGA', fasta_sequence[i:])

        for seq in ORF_sequences_TGA:

            if len(seq) > 1 and len(seq) % 3 == 0:

                ORF_sequences.append(seq)

        ORF_sequences_TAA = re.findall('^ATG[ACGT]+TAA', fasta_sequence[i:])

        for seq in ORF_sequences_TAA:

            if len(seq) > 1 and len(seq) % 3 == 0:

                ORF_sequences.append(seq)

    char = 'a'
    ORF_sequence = char * 999999

    for seq in ORF_sequences:

        if len(seq) < len(ORF_sequence):

            ORF_sequence = seq

    sft(ORF_sequence)