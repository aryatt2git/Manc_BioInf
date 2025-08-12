import DNA2Prot
import reverse_seq

def six_frame_trans(sequence):
    '''
    This function converts the input sequence into an amino acid sequence using the DNA2Prot function. The reverse
    complementary sequence is then converted to an amino acid sequence using reverse_seq functions and DNA2Prot
    functions.

    The function shifts the open-reading frame by one nucleotide position forward and repeats the process. This
    occurs two more times after the first nucleotide position in the input sequence, generating 3 forward and 3
    reverse amino acid sequences.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'aggagtaagcccttgcaactggaaatacacccattg'

    :return: forwards: a list of 3 sequences of amino acids encoded by the open-reading frame of the input sequence,
                       starting at the 1st, 2nd and 3rd nucleotide positions.
                       E.g. ['AETSWTGDRLWGFSDNWPALRRPSP', 'LRLPGRGTGCGVSQITGPLRSGGLH', '*DFLDGGQAVGFLR*LGPCAQEFT']

             reverses: a list of 3 sequences of amino acids encoded by the reverse of the sequence,
                       complementary to the input sequence, starting at the 1st, 2nd and 3rd nucleotide positions.
                       E.g. ['G*RPPERRGPVI*ETPQPVPRPGSLS', 'GEGLLSAGQLSEKPHSLSPVQEVS', 'VKS*AQGPSYLRNPTCPPSRKSQ']

    :command: sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
              six_frame_trans(sequence)
    '''

    # An empty list to be populated with strings of amino acids encoded by the input sequence.
    forwards = []

    # An empty list to be populated with strings of amino acids encoded by the reverse of the sequence, complementary to the input sequence.
    reverses = []

    # This loop iterates through the 1st, 2nd and 3rd positions of the input sequence.
    for i in range(0, 3):

        # It assigns the open-reading frame, starting from either the 1st, 2nd or 3rd position to the end of the input sequence, to the 'input_seq' variable.
        input_seq = sequence[i:len(sequence)]

        # The DNA2Prot function is used to convert the open-reading frame into a corresponding amino acid sequence.
        forw_prot_seq = DNA2Prot(input_seq)

        # The amino acid seuqence is then added to the 'forwards' list.
        forwards.append(forw_prot_seq)

        # The reverse of the complimentary sequence to the input sequence frame is generated using the reverse_seq function.
        # The dimensions at the end iterate through the 1st, 2nd and 3rd positions in the reverse strand.
        rev_prot_seq = reverse_seq(sequence)[i:len(sequence)]

        # The DNA2Prot function is used to convert the reverse sequence into a corresponding amino acid sequence.
        reverses.append(DNA2Prot(rev_prot_seq))

    # The loop prints each forward amino acid sequence to screen.
    print('Forward')
    for seq in forwards:
        print(seq)

    # The loop prints each reverse amino acid sequence to screen.
    print('Reverse')
    for seq in reverses:
        print(seq)

    # The 'forwards' and 'reverses' lists are returned.
    return forwards, reverses