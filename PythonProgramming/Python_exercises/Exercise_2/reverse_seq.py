def reverse_seq(sequence):
    '''
    This function returns the complementary sequence to a sequence of nucleotides in reverse order, so it still
    reads from 5' -> 3'.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'aggagtaagcccttgcaactggaaatacacccattg'

    :return: a string of nucleotides complementary to the reverse order of the input sequence.
             E.g. 'caatgggtgtatttccagttgcaagggcttactcct'

    :command: sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
              reverse_seq(sequence)
    '''

    # Prepares an empty string which can be populated with a sequence of nucleotides, complementary to the reverse of the input sequence.
    rev_comp_seq = ''

    # This reverses the input sequence, converts the letters into lowercase and removes any whitespace.
    reversed_seq = sequence[::-1].lower().replace(' ', '')

    # This loop iterates through each nucleotide in the reverse sequence and applies a condition.
    for nucleotide in reversed_seq:

        # If the nucleotide is an 'a', a 't' is appended to the complementary string.
        if nucleotide == 'a':
            rev_comp_seq += 't'

        # If the nucleotide is a 't', an 'a' is appended to the complementary string.
        elif nucleotide == 't':
            rev_comp_seq += 'a'

        # If the nucleotide is a 'g', a 'c' is appended to the complementary string.
        elif nucleotide == 'g':
            rev_comp_seq += 'c'

        # If the nucleotide is a 'c', a 'g' is appended to the complementary string.
        elif nucleotide == 'c':
            rev_comp_seq += 'g'

        # If the nucleotide is not 'a', 't', 'c' or 'g', an 'N' is appended to the complementary string.
        else:
            rev_comp_seq += 'N'

    # The  reverse complementary sequence is printed to screen.
    print(rev_comp_seq)

    # The reverse complementary sequence is returned
    return rev_comp_seq