def chunk_sequence(sequence, chunk_length):
    '''
        This function converts a sequence into chunks of the same length, where rows are 60 characters long and are split into fragments
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

    for codon in range(0, len(sequence) + 3, 3):
        print(sequence[codon - 3:codon], end=' ')
