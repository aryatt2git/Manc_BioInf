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

    for i in range(len(fasta_sequence)):

        ORF_sequences_TAG = re.findall('^ATG[ACGT]+TAG', fasta_sequence[i:])

        for seq in ORF_sequences_TAG:

            print('TAG: ', len(seq))

            if len(seq) % 3 == 0:

                ORF_sequences.append(seq)

        ORF_sequences_TGA = re.findall('^ATG[ACGT]+TGA', fasta_sequence[i:])

        for seq in ORF_sequences_TGA:

            print('TGA: ', len(seq))

            if len(seq) % 3 == 0:

                ORF_sequences.append(seq)

        ORF_sequences_TAA = re.findall('^ATG[ACGT]+TAA', fasta_sequence[i:])

        for seq in ORF_sequences_TAA:

            print('TAA: ', len(seq))

            if len(seq) % 3 == 0:

                ORF_sequences.append(seq)

    char = 'a'
    ORF_sequence = char * 999999

    for seq in ORF_sequences:

        if len(seq) < len(ORF_sequence):

            ORF_sequence = seq

    sft(ORF_sequence)