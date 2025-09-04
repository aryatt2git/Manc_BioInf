def chunk_sequence(sequence, chunk_length):
    '''
    This function slices a sequence into chunks of the same length. The user can define the length of the chunk.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'aggagtaagcccttgcaactggaaatacacccattg'

    :return: a DNA sequence in chunks of 3 characters in length.
             E.g. AGG AGT AAG CCC TTG CAA CTG GAA ATA CAC CCA TTG

    :command: sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
              convert2fasta(sequence, 3)
    '''

    # An empty string in which to store the chunks that the sequence has been separated in to.
    chunked_sequence = ''

    # This iterates through all of the multiples of the chunk length, as defined by the user, up to the total length of the input sequence.
    for chunk in range(0, len(sequence) + chunk_length, chunk_length):

        # The for loop slices the sequence at every position where the chunk length is a multiple, thereby splitting the sequence into chunks of the same length. Each chunk is appended to the 'chunked_sequence' string.
        chunked_sequence += f'{sequence[chunk - chunk_length:chunk]} '.upper()

    # The chunked_sequence is printed to screen.
    print(chunked_sequence.strip())

    # The chunked_sequence is returned from the function.
    return chunked_sequence.strip()