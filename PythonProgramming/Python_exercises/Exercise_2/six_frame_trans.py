def six_frame_trans(sequence):
    forwards = []
    reverses = []

    for i in range(0, 3):
        input_seq = sequence[i:len(sequence)]

        forw_prot_seq = DNA2Prot(input_seq)

        forwards.append(forw_prot_seq)

        rev_prot_seq = reverse_seq(sequence)[i:len(sequence)]

        reverses.append(DNA2Prot(rev_prot_seq))

    print('Forward')
    for seq in forwards:
        print(seq)

    print('Reverse')
    for seq in reverses:
        print(seq)

    return forwards, reverses