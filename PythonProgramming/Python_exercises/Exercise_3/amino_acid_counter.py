import os
import sys
from logger import logger

def amino_acid_counter():
    '''
    This interactive script counts the number of times an amino acid appears in a file. The script provides an
    interface that allows the user to specify the file to search in and the amino acid to search for. The amino
    acid input should be a 3-letter abbreviation of the amino acid.

    N.B. This script should be activated from the terminal command line.

    :command: python3 path/to/this/script/from/current/working/directory/amino_acid_counter.py
    '''

    # An INFO message is printed to the .log file that shows that the script has been activated.
    logger.info('amino_acid_counter.py script initiated.')

    # A banner to indicate that the script has been activated.
    print('<<<<<<<<<<<<<<<<<AMINO ACID COUNTER ACTIVATED>>>>>>>>>>>>>>>>>\n')

    # A warning note asking the user to ensure that the file containing the amino acids is in the same directory as the script. This is so the file can be found.
    print('**  WARNING: PLEASE ENSURE THE FILE WITH AMINO ACIDS IS IN  **\n'
          '          **  THE SAME DIRECTORY AS THE SCRIPT.  **\n')

    # The 'while' loop enables the script to return to this point so that the user can make multiple attempts to enter a valid filename.
    while True:

        # The 'input' function is used to allow the user to enter a filename. It also includes a prompt to instruct the user.
        filename = input('Please enter a filename or type "quit" to quit:\n').strip()

        # This uses 'getcwd()' from the os module to find the path to the directory that the script was executed from.
        filepath_part_one = os.getcwd()

        # The 'argv' function from the 'sys' module returns the filepath to the script, entered on the commandline to initiate the script.
        script = sys.argv[0]

        # An empty string is prepared to be populated by the names of the directories between the current working directory and the directory containing the file and script.
        filepath_part_two = ''

        # A 'for' loop that iterates through each directory in the filepath from the current working directory and the directory containing script.
        for directory in script.split('/')[:-1]:

            # Each directory between the working directory and the directory containing the script is added to the string.
            filepath_part_two = filepath_part_two + f'{directory}/'

        # The file is searched for within the same directory that the script was executed from.
        file = f'{filepath_part_one}/{filepath_part_two}{filename}'

        # The filename is converted to lowercase to see if it matches with the word 'quit'. If it does, the script terminates.
        # Quitting the script takes priority over any other condition in the 'while' loop so it is placed first.
        if filename.lower() == 'quit':

            print('---------------------------------\n'
                  '<<<<<<<<<<<<<<<<<AMINO ACID COUNTER TERMINATED>>>>>>>>>>>>>>>>\n')

            # An INFO message is printed to the .log file, stating that the script has been terminated at the Filename input stage.
            logger.info('Filename input: User terminated the script.')

            # 'return' breaks the 'while' loop and ends the function, thereby terminating the script.
            return

        # The second most important input to consider is when there is no input. If an input is not entered, the prompt prints 'No input received.' to the terminal screen, notifying the user to enter something instead of nothing.
        elif len(filename) == 0:
            print('---------------------------------\nNo input received.')

            # An ERROR message is printed to the .log file, stating that the user did not enter anything at the Filename input stage.
            logger.error('Filename input: User did not enter anything.')

        # A condition to determine if the user did not distinguish the file extension when they entered the Filename.
        elif '.' not in filename:

            # A message to help the user is printed to the terminal.
            print("---------------------------------\nEither '.' was missing from the filename or the file extension was not included.")

            # An ERROR message is printed to the .log file, stating that the user did not enter a valid file extension at the Filename input stage.
            logger.error(f'Filename input: User did not enter a valid file extension. User entered: {filename}')

        # The 'path.exists' function from the 'os' module determines if the filepath and filename entered by the user truly exists. If they are, then a prompt notifies the user that it was valid.
        elif os.path.exists(file):
            print('\n<<<<<<<<<<<<<<<<<<<<<<<<<OPENING FILE>>>>>>>>>>>>>>>>>>>>>>>>>')

            # An INFO message is printed to the .log file, stating that the user did not enter anything at the Filename input stage.
            logger.info(f'Filename input: User entered a valid filename: {filename}')

            # The 'break' keyword is used instead of 'return' because it exits the 'while' loop without deactivating the script.
            break

        # I anything else is entered, then a simple prompt, 'File cannot be found.', is printed to screen, notifying the user that there is a problem with their input.
        # I think further development should be made to help user identify why their input did not work as both the filename and filepath need to be correct.
        else:
            print('---------------------------------\nFile could not be found.')

            # An ERROR message is printed to the .log file, stating that the user did not enter a valid filename at the Filename input stage.
            logger.error(f'Filename input: User did not enter a valid filename. User entered: {filename}')

    # A list of 3-letter abbreviations of all 20 amino acids that can be iterated through.
    amino_acids_list = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS',
                        'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP',
                        'TYR', 'VAL']

    # A DEBUG message is printed to the .log file, to show that the user has successfully accessed a file and is now going to search for an amino acid in it.
    logger.debug('User can now search for the amino acid.')

    # The 'while' loop enables the script to return to this point so that the user can make multiple attempts to enter a valid abbreviation or the 'SECRET PASSWORD'.
    while True:

        # The user is asked to enter a 3-letter abbreviation of an amino acid to search for in the file. The input if converted into uppercase and whitespace is removed before and after.
        amino_acid = input('Please enter a 3-letter abbreviation of an amino acid '
                           'OR the ***SECRET PASSWORD***\n...or type "quit" to quit:\n').upper().strip()

        # A counter incorporated into a 'for' loop to count the number of times each amino acid occurs in the file.
        amino_acid_number = 0

        # A condition that allows the user to enter 'quit' to terminate the script.
        if amino_acid == 'QUIT':
            print('---------------------------------\n'
                  '<<<<<<<<<<<<<<<<<AMINO ACID COUNTER TERMINATED>>>>>>>>>>>>>>>\n')

            # An INFO message is printed to the .log file, stating that the script has been terminated at the Amino acid input stage.
            logger.info('Amino Acid input: User terminated the script.')

            # 'return' breaks the 'while' loop and ends the function, thereby terminating the script.
            return

        # A condition to accept the secret password 'SHOW ME THE MONEY'.
        elif amino_acid == 'SHOW ME THE MONEY':

            # An INFO message printed to the .log file, stating that the User has entered the secret password, giving them a full amino acid count.
            logger.info('Amino Acid input: User entered the secret password.')

            print('\n<<<<<<<<<<<<<<<<<<<<<<<PASSWORD ACCEPTED>>>>>>>>>>>>>>>>>>>>>>')

            # Opens the file specified by the user in the first input.
            with open(file) as open_file:

                # Create an empty dictionary in which to store all of the amino acids found in the file along with their frequencies.
                aa_count_dict = {}

                # Iterate through each line in the file.
                for line in open_file:

                    # A condition to find the 3-letter amino acid abbreviation, 3 positions from the end of the line after whitespace has been removed from the beginning and end of the line.
                    if len(line.strip().split(' ')[-3]) == 3:
                        aa = line.strip().split(' ')[-3]

                    # A condition to find the 3-letter amino acid abbreviation, 2 positions from the end of the line after whitespace has been removed from the beginning and end of the line.
                    elif len(line.strip().split(' ')[-2]) == 3:
                        aa = line.strip().split(' ')[-2]

                    else:
                        continue

                    # A condition to add the amino acid from the file to the dictionary it has not been added already.
                    if aa not in aa_count_dict.keys():

                        # The frequency for the newly added amino acid is changed to 1.
                        aa_count_dict[aa] = 1

                    # A condition to increase the amino acid count by 1, if it has already been added to the dictionary.
                    elif aa in aa_count_dict.keys():

                        aa_count_dict[aa] = aa_count_dict[aa] + 1

                # A 'for' loop that prints the amino acids to screen, if their count is higher than 1.
                for item in aa_count_dict:

                    if aa_count_dict[item] > 0:

                        print(f'{item}: {aa_count_dict[item]}')

                print('---------------------------------')

        # If an input is not entered, the prompt prints 'No input received.' to the terminal screen, notifying the user to enter something instead of nothing.
        elif len(amino_acid) == 0:
            print('---------------------------------\nNo input received.')

            # An ERROR message is printed to the .log file, stating that the user did not enter anything at the Amino Acid input stage.
            logger.error('Amino Acid input: User did not enter anything.')

        # And if the amino acid entered by the user is not 3 characters long, the prompt, 'Abbreviation should be 3 letters long.' is printed to screen.
        elif len(amino_acid) != 3:
            print('---------------------------------\nAbbreviation should be 3 letters long.')

            # An ERROR message is printed to the .log file, stating that the user did not enter an amino acid abbreviation 3 letters long.
            logger.error(f'Amino Acid input: User did not enter an abbreviation 3 letters long. User entered: {amino_acid}')

        # And if the amino acid is not recognised, i.e. it is not in the amino acid list, the prompt, 'Input does not correspond with an amino acid abbreviation.' is printed to screen.
        elif amino_acid not in amino_acids_list:
            print('---------------------------------\nInput does not correspond with an amino acid abbreviation.')

            # An ERROR message is printed to the .log file, stating that the user did not enter a valid amino acid abbreviation.
            logger.error(f'Amino Acid input: User did not enter a valid amino acid abbreviation. User entered: {amino_acid}')

        # But if the amino acid entered by the user is in the amino acid list, the file specified by the user is opened and each line is iterated through in search for that amino acid.
        elif amino_acid in amino_acids_list:

            # An INFO message is printed to the .log file, stating which amino acid abbreviation the user searched for.
            logger.info(f'Amino Acid input: User successfully searched for {amino_acid}')

            with open(file) as open_file:

                for line in open_file:

                    # If the amino acid is in the line, the amino acid counter increases by 1.
                    if amino_acid in line:

                        amino_acid_number = amino_acid_number + 1

                # A message is printed to screen informing the user of how many times the amino acid they are searching for appears in the file that they specified.
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      f'{amino_acid} appears in {filename} {amino_acid_number} times.\n'
                      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

                # A DEBUG message is printed to the .log file, restating the output from the script.
                logger.debug(f'Amino Acid output: {amino_acid} appears in {filename} {amino_acid_number} times.')

        # If the user's input does not conform with previous conditions, the prompt 'Input does not correspond with an amino acid abbreviation.' is printed to screen and the user is able to try again.
        else:
            print('---------------------------------\nInput does not correspond with an amino acid abbreviation.')

            for char in amino_acid:
                print(type(char))


# This condition  allows the script to be initiated from the command line.
if __name__ == '__main__':
    amino_acid_counter()