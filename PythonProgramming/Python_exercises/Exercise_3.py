# 3.1

import os

def open_file():

    while True:

        filename = input('Please enter filename or type "quit" to quit:')

        filepath = os.getcwd()

        file = f'{filepath}/PythonProgramming/Python_exercises/{filename}'

        if filename == 'quit':
            print('---------------------------------\nTerminating script...')
            return

        elif len(filename) == 0:
            print('---------------------------------\nNo input received.')

        elif os.path.exists(file):
            print('Opening file...')
            break

        else:
            print('---------------------------------\nFile cannot be found.')

    amino_acids_list = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']

    while True:

        amino_acid = input('Please enter a 3-letter abbreviation of an amino acid OR the ***SECRET PASSWORD***\n...or type "quit" to quit:').upper()

        amino_acid_number = 0

        if amino_acid == 'QUIT':
            print('---------------------------------\nTerminating script...')
            return

        if amino_acid == 'SHOW ME THE MONEY':

            print('<<<<<<<<<<<<<<<<<<<<<<PASSWORD ACCEPTED>>>>>>>>>>>>>>>>>>>>>>')

            with open(file) as open_file:

                aa_count_dict = {}

                for line in open_file:

                    aa = line[15:18]

                    if aa not in aa_count_dict.keys():

                        aa_count_dict[aa] = 1

                    elif aa in aa_count_dict.keys():

                        aa_count_dict[aa] = aa_count_dict[aa] + 1

                for item in aa_count_dict:

                    if aa_count_dict[item] > 0:

                        print(f'{item}: {aa_count_dict[item]}')

                print('---------------------------------')

        elif len(amino_acid) == 0:
            print('---------------------------------\nNo input received.')

        elif len(amino_acid) != 3:
            print('---------------------------------\nAbbreviation should be 3 letters long.')

        elif amino_acid not in amino_acids_list:
            print('---------------------------------\nInput does not correspond with an amino acid abbreviation.')

        elif amino_acid in amino_acids_list:

            with open(file) as open_file:

                for line in open_file:

                    if amino_acid in line:

                        amino_acid_number = amino_acid_number + 1

                print(f'{amino_acid} appears in {filename} {amino_acid_number} times.\n---------------------------------')

        else:
            print('---------------------------------\nInput does not correspond with an amino acid abbreviation.')

open_file()