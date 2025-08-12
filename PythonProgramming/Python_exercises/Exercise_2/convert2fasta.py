def convert2fasta(sequence):
    '''
    This function converts a sequence to FASTA format, where rows are 60 characters long and are split into fragments
    that are 10 characters in length. Therefore, each row consists of 6 fragments of sequence. Each line begins with
    the positional coordinate of the first nucleotide in the row.

    :params: sequence: a string of any number of nucleotides [A, T, C, G] in any order.
                       E.g. 'GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG'

    :return: a DNA sequence in FASTA format.
              E.g. 1	gctgagactt	cctggacggg	ggacaggctg	tggggtttct	cagataactg	ggcccctgcg
                  61	ctcaggaggc	cttcaccctc	tgctctgggt	aaagttcatt	ggaacagaaa	gaaatggatt
                 121	tatctgctct	tcgcgttgaa	gaagtacaaa	atgtcattaa	tgctatgcag	aaaatcttag
                 181	agtgtcccat	ctgtctggag	ttgatcaagg	aacctgtctc	cacaaagtgt	gaccacatat
                 241	tttgcaaatt	ttgcatgctg	aaacttctca	accagaagaa	agggccttca	cagtgtcctt
                 301	tatgtaagaa	tgatataacc	aaaaggagcc	tacaagaaag	tacgagattt	agtcaacttg
                 361	ttgaagagct	attgaaaatc	atttgtgctt	ttcagcttga	cacaggtttg	gagtatgcaa
                 421	acagctataa	ttttgcaaaa	aaggaaaata	actctcctga	acatctaaaa	gatgaagttt
                 481	ctatcatcca	aagtatgggc	tacagaaacc	gtgccaaaag	acttctacag	agtgaacccg
                 541	aaaatccttc	cttgcaggaa	accagtctca	gtgtccaact	ctctaacctt	ggaactgtga
                 601	gaactctgag	gacaaagcag	cggatacaac	ctcaaaagac	gtctgtctac	attgaattgg
                 661	gatctgattc	ttctgaagat	accgttaata	aggcaactta	ttgcagtgtg	ggagatcaag

    :command: sequence = 'GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAG'
              convert2fasta(sequence)
    '''

    # An empty string in which the sequence can be stored in fasta format.
    fasta = ''

    # A loop to separate the input sequence into blocks of 60 characters long, distinguishing each row that will be iterated through.
    for row in range(60, len(sequence) + 60, 60):

        # The start coordinate is generated, followed by a tab to separate it from the start of the first fragment. The coordinate is right-justified.
        start_coordinate = f'{str(row - 59).rjust(len( str( len(sequence) + 60 )))}\t'

        # The start coordinate is the first thing added to the new line.
        fasta = fasta + start_coordinate

        # The nucleotide sequence of that row is assigned to the 'row_sequence' variable.
        row_sequence = f'{sequence[row-60:row].lower()}'

        # This loop determines which positions the row should be split at and iterates through each fragment.
        for fragments in range(10, len(row_sequence) + 10, 10):

            # A tab is added to the end of each fragment to make it distinguishable from the following fragment.
            split_sequence = f'{row_sequence[fragments-10:fragments]}\t'

            # The fragment is appended to the end of the FASTA string.
            fasta = fasta + split_sequence

        # A newline is created at the end of the row to distinguish each row.
        fasta = fasta + '\n'

    # The sequence is printed to screen in FASTA format.
    print(fasta)

    # The FASTA sequence is returned.
    return fasta