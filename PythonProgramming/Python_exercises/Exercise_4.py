# 4

import os
import re

filename = 'U15422.1.fasta'

filepath = os.getcwd()

file = f'{filepath}/PythonProgramming/Python_exercises/{filename}'

raw_fasta_sequence = ''

with open(file) as fasta_file:

    next(fasta_file)

    for lines in fasta_file:

        raw_fasta_sequence = raw_fasta_sequence + lines

    fasta_sequence = raw_fasta_sequence.replace('\n', '')

    for i in range(len(fasta_sequence)):

       ORF_sequences = re.search('^ATG[ACGT]+TAG|ATG[ACGT]+TGA|ATG[ACGT]+TAA', fasta_sequence[i:])

       #if len(ORF_sequences) > 0:
       print(ORF_sequences)#[0][0:3], '...', ORF_sequences[0][-3:])
                #print(ORF_sequences[0][0:3], '...', ORF_sequences[0][-3:] , '...', len(ORF_sequences[0]))
            
            # and len(ORF_sequences) % 3 == 0