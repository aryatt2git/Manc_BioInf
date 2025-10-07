import pytest
from modules.convert2fasta import convert2fasta

@pytest.mark.parametrize('sequence, row_len, fragment_len, expected', [
        ('tatcggctacatgtaccgtatcga', 8, 2, ' 1\tta\ttc\tgg\tct\t\n'
                                           ' 9\tac\tat\tgt\tac\t\n'
                                           '17\tcg\tta\ttc\tga\t\n'),           # checks normal function
        ('TATCGGCTACATGTACCGTATCGA', 8, 2, ' 1\tta\ttc\tgg\tct\t\n'
                                           ' 9\tac\tat\tgt\tac\t\n'
                                           '17\tcg\tta\ttc\tga\t\n'),           # maybe function converts to uppercase
        ('', 8, 2, ''),                                                         # empty input returns empty list
        ('TATCGGCT', 10, 3, ' 1\ttat\tcgg\tct\t\n'),                            # row length > sequence length
        ('TATCGGCT', 4, 4, ' 1\ttatc\t\n'
                           ' 5\tggct\t\n'),                                     # row_len == seq length
        ('ATCG', 4, 1, '1\ta\tt\tc\tg\t\n'),                                    # chunk size = 1
])

def test_convert2fasta(sequence, row_len, fragment_len, expected):

    output = convert2fasta(sequence, row_len, fragment_len)

    assert output == expected

def test_invalid_chunk_sequence():
    with pytest.raises(AssertionError) as exc_info:
        chunk_sequence('ATBXZ', 2)
    assert exc_info.value.args[0] == 'B at position 3 in the sequence is not a nucleotide.'

def test_chunk_length():
    with pytest.raises(AssertionError):
        chunk_sequence('ATCG', 0)
    with pytest.raises(AssertionError):
        chunk_sequence('ATCG', -1)
    with pytest.raises(TypeError):
        chunk_sequence('ATCG',)
    with pytest.raises(TypeError):
        chunk_sequence('ATCG')
    with pytest.raises(TypeError):
        chunk_sequence('ATCG', 'ATCG')

def test_other_data_types():
    with pytest.raises(AssertionError) as exc_info:
        chunk_sequence(12345, 3)
    assert exc_info.value.args[0] == 'sequence is not a string.'

    with pytest.raises(AssertionError) as exc_info:
        chunk_sequence(None, 3)
    assert exc_info.value.args[0] == 'sequence is not a string.'

    with pytest.raises(AssertionError) as exc_info:
        chunk_sequence(['A', 'T'], 3)
    assert exc_info.value.args[0] == 'sequence is not a string.'