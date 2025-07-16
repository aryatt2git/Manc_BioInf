# 3.1

# a)

def open_file():

    import os

    while True:

        filename = input('Please enter filename:')

        filepath = os.getcwd()

        file = f'{filepath}/PythonProgramming/Python_exercises/{filename}'

        if filename == 'quit':
            print('Terminating script...')
            return

        elif len(filename) == 0:
            print('No input received. Please enter a filename or type "quit" to quit:')

        elif os.path.exists(file):

            print('Opening file...')

            open_file = open(file)
            break

        else:
            print('File cannot be found. Please check that the filename is correct or type "quit" to quit:')

    while True:

        amino_acid = input('Please enter a 3-letter abbreviation of an amino acid:').upper()

        amino_acids_list = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']

        amino_acid_number = 0

        if amino_acid == 'QUIT':
            print('Terminating script...')
            return

        elif len(amino_acid) == 0:
            print('No input received. Please enter one of the following abbreviations or type "quit" to quit:', amino_acids_list)

        elif len(amino_acid) != 3:
            print('Abbreviation should be 3 letters long. Please try again or type "quit" to quit:')

        elif amino_acid not in amino_acids_list:

            print('Input does not correspond with an amino acid abbreviation. Please enter one of the following abbreviations or type "quit" to quit:', amino_acids_list)

        elif amino_acid in amino_acids_list:

            for line in open_file:

                if amino_acid in line:

                    amino_acid_number = amino_acid_number + 1

            break

        else:
            print('Input does not correspond with an amino acid abbreviation. Please enter one of the following abbreviations or type "quit" to quit:', amino_acids_list)

    while amino_acid in amino_acids_list:

        print(f'{amino_acid} appears in {filename} {amino_acid_number} times.')
        break

open_file()