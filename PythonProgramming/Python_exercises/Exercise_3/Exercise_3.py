# 3.1

import os

def amino_acid_count():
    '''
    This interactive script counts the number of times an amino acid appears in a file. The script provides an
    interface that allows the user to specify the file to search in and the amino acid to search for. The amino
    acid input should be a 3-letter abbreviation of the amino acid.
    '''

    # A banner to indicate that the script has been activated.
    print('<<<<<<<<<<<<<<<<<AMINO ACID COUNTER ACTIVATED>>>>>>>>>>>>>>>>>')

    # The 'while' loop enables the script to return to this point so that the user can make multiple attempts to enter a valid filename.
    while True:

        # The 'input' function is used to allow the user to enter a filename. It also includes a prompt to instruct the user.
        filename = input('Please enter a filename or type "quit" to quit:\n').strip()

        filepath = os.getcwd()

        file = f'./{filename}'

        # The filename is converted to lowercase to see if it matches with the word 'quit'. If it does, the script terminates.
        # Quitting the script takes priority over any other condition in the 'while' loop so it is placed first.
        if filename.lower() == 'quit':

            print('---------------------------------\n'
                  '<<<<<<<<<<<<<<<<<AMINO ACID COUNTER TERMINATED>>>>>>>>>>>>>>>>\n')

            # 'return' breaks the 'while' loop and ends the function, there by terminating the script.
            return

        # The second most important input to consider is when there is no input. If an input is not entered, the prompt prints 'No input received.' to the terminal screen, notifying the user to enter something instead of nothing.
        elif len(filename) == 0:
            print('---------------------------------\nNo input received.')

        # The 'path.exists' function from the 'os' module determines if the filepath and filename entered by the user truly exists. If they are, then a prompt notifies the user that it was valid.
        elif os.path.exists(file):
            print('\n<<<<<<<<<<<<<<<<<<<<<<<<<OPENING FILE>>>>>>>>>>>>>>>>>>>>>>>>>')

            # The 'break' keyword is used instead of 'return' because it exits the 'while' loop without deactivating the script.
            break

        # I anything else is entered, then a simple prompt, 'File cannot be found.', is printed to screen, notifying the user that there is a problem with their input.
        # I think further development should be made to help user identify the nature of why their input did not work as both the filename and filepath need to be correct.
        else:
            print('---------------------------------\nFile cannot be found.')

    amino_acids_list = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS',
                        'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP',
                        'TYR', 'VAL']

    while True:

        amino_acid = input('Please enter a 3-letter abbreviation of an amino acid '
                           'OR the ***SECRET PASSWORD***\n...or type "quit" to quit:\n').upper().strip()

        amino_acid_number = 0

        if amino_acid == 'QUIT':
            print('---------------------------------\n'
                  '<<<<<<<<<<<<<<<<<AMINO ACID COUNTER TERMINATED>>>>>>>>>>>>>>>\n')
            return

        if amino_acid == 'SHOW ME THE MONEY':

            print('\n<<<<<<<<<<<<<<<<<<<<<<<PASSWORD ACCEPTED>>>>>>>>>>>>>>>>>>>>>>')

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

                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      f'{amino_acid} appears in {filename} {amino_acid_number} times.\n'
                      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        else:
            print('---------------------------------\nInput does not correspond with an amino acid abbreviation.')

if __name__ == '__main__':
    amino_acid_count()