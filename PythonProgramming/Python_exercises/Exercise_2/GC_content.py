import nucleotide_count

def GC_content(sequence):
    '''
    The function uses the nucleotide_count function to find the number of G and C residues in a given sequence. It
    then calculates the proportion of the input sequence is occupied by G or C residues and presents the proportion
    as a percentage of the input sequence.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'aggagtaagcccttgcaactggaaatacacccattg'

    :return: The GC content percentage to 2 decimal places.
             E.g. 47.22

    :command: sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
              GC_content(sequence)
    '''

    # A dictionary with each nucleotide type as a key and their frequency within the input string as their respective values.
    nucleotide_count_dict = nucleotide_count(sequence, 1)

    # The frequencies of the 'G' and 'C' residues in the input string are added together and divided by the total number of residues in the string. It is then multiplied by 100 to give the percentage.
    GC_cont = ((nucleotide_count_dict['G'] + nucleotide_count_dict['C']) / len(sequence)) * 100

    # The GC content percentage is shortened to 2 decimal places.
    GC_percent = '{:.2f}'.format(GC_cont)

    # The percentage is incorporated at the end of statement 'The GC content is ' which is printed to screen.
    print(f'The GC content is {GC_percent}%')

    # The GC content percentage to 2 decimal places is returned as an integer data type.
    return GC_percent