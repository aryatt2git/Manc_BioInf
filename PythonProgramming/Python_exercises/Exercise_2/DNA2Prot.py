def DNA2Prot(sequence):
    '''
    This function reads each trinucleotide codon in a DNA sequence and converts it in to a corresponding amino acid.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'aggagtaagcccttgcaactggaaatacacccattg'

    :return: a string of amino acids.
             E.g. 'MDLSALRVEEVQNVINAMQKILECPICLELIKEPVSTKCDHIFCKFCMLKLLNQKKGPSQCPLCKNDITK'

    :command: sequence = 'aggagtaagcccttgcaactggaaatacacccattg'
              DNA2Prot(sequence)
    '''

    # The sequence is converted into uppercase and white spaces are removed.
    DNA_sequence = sequence.upper().replace(' ', '')

    # A dictionary of amino acids with single-character representations of each amino acid as keys and a list of corresponding codons that encode the amino acid, as a value.
    trans_seq = {}
    trans_seq['F'] = ['TTT', 'TTC']
    trans_seq['L'] = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
    trans_seq['I'] = ['ATT', 'ATC', 'ATA']
    trans_seq['M'] = ['ATG']
    trans_seq['V'] = ['GTT', 'GTC', 'GTA', 'GTG']
    trans_seq['S'] = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
    trans_seq['P'] = ['CCT', 'CCC', 'CCA', 'CCG']
    trans_seq['T'] = ['ACT', 'ACC', 'ACA', 'ACG']
    trans_seq['A'] = ['GCT', 'GCT', 'GCA', 'GCG']
    trans_seq['Y'] = ['TAT', 'TAC']
    trans_seq['*'] = ['TAA', 'TAG', 'TGA']
    trans_seq['H'] = ['CAT', 'CAC']
    trans_seq['Q'] = ['CAA', 'CAG']
    trans_seq['N'] = ['AAT', 'AAC']
    trans_seq['K'] = ['AAA', 'AAG']
    trans_seq['D'] = ['GAT', 'GAC']
    trans_seq['E'] = ['GAA', 'GAG']
    trans_seq['C'] = ['TGT', 'TGC']
    trans_seq['W'] = ['TGG']
    trans_seq['R'] = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
    trans_seq['G'] = ['GGT', 'GGC', 'GGA', 'GGG']

    # This prepares a string that can be populated by single-letter representations of amino acids.
    protein_sequence = ''

    # This loop reads every 3 nucleotides in the sequence, starting from the first position in the string.
    for position in range(3, len(DNA_sequence) + 3, 3):

        codon = DNA_sequence[position - 3: position]

        # This loop determines if any of the nucleotides in the codon are not A, C, G or T.
        for nucleotide in codon:
            if nucleotide not in ['A', 'C', 'G', 'T']:

                # If the condition is fulfilled, the comment '-codon not recognised-' is appended to the protein sequence string.
                protein_sequence += '-codon not recognised-'

        # This loop iterates through the amino acid dictionary and assigns each amino acid and list of codons to a tuple of 'key' and 'value' variables.
        for key, value in trans_seq.items():

            # This condition determines if a codon is present in the amino acid dictionary's values and appends the corresponding key (single-letter amino acid) to the protein sequence string.
            if codon in value:
                protein_sequence += key

        # This condition determines if the codon length (usually at the end of original nucleotide sequence) is less than 3 and therefore, cannot represent a codon.
        if len(codon) < 3:

            # If the condition is fulfilled, the comment '-end of sequence out of frame' is appended to the protein sequence string.
            protein_sequence += '-end of sequence out of frame'

    # The final protein sequence is printed to screen.
    print(protein_sequence)

    #The protein sequence is returned.
    return protein_sequence