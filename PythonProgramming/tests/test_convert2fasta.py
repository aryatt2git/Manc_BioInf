import pytest
from modules.convert2fasta import convert2fasta

@pytest.mark.parametrize('sequence, row_len, fragment_len, expected', [
        ('tatcggctacatgtaccgtatcga', 8, 2, ' 1\tta\ttc\tgg\tct\t\n'             # checks normal function
                                           ' 9\tac\tat\tgt\tac\t\n'
                                           '17\tcg\tta\ttc\tga\t\n'),
        ('TATCGGCTACATGTACCGTATCGA', 8, 2, ' 1\tta\ttc\tgg\tct\t\n'             # maybe function converts to uppercase
                                           ' 9\tac\tat\tgt\tac\t\n'
                                           '17\tcg\tta\ttc\tga\t\n'),
        ('', 8, 2, ''),                                                         # empty input returns empty list
        ('TATCGGCT', 10, 3, ' 1\ttat\tcgg\tct\t\n'),                            # row length > sequence length
        ('TATCGGCT', 4, 4, ' 1\ttatc\t\n'                                       # row_len == seq length
                           ' 5\tggct\t\n'),
        ('ATCG', 4, 1, '1\ta\tt\tc\tg\t\n'),                                    # chunk size = 1
])

def test_convert2fasta(sequence, row_len, fragment_len, expected):

    output = convert2fasta(sequence, row_len, fragment_len)

    assert output == expected

def test_invalid_sequence():
    with pytest.raises(AssertionError) as exc_info:
        convert2fasta('ATBXZ', 4, 2)
    assert exc_info.value.args[0] == 'B at position 3 in the sequence is not a nucleotide.'

def test_row_fragment_len():
    with pytest.raises(AssertionError):
        convert2fasta('ATCGA', 0, 5)
    with pytest.raises(AssertionError):
        convert2fasta('ATCGA', -1, 5)
    with pytest.raises(AssertionError):
        convert2fasta('ATCGA', 5, 0)
    with pytest.raises(AssertionError):
        convert2fasta('ATCGA', 5, -1)
    with pytest.raises(AssertionError):
        convert2fasta('ATCGA', 0, 0)
    with pytest.raises(TypeError):
        convert2fasta('ATCGA',)
    with pytest.raises(TypeError):
        convert2fasta('ATCGA')
    with pytest.raises(TypeError):
        convert2fasta('ATCGA', 'ATCGA', 'ATCGA')

def test_other_data_types():
    with pytest.raises(AssertionError) as exc_info:
        convert2fasta(12345, 3, 1)
    assert exc_info.value.args[0] == 'sequence is not a string.'

    with pytest.raises(AssertionError) as exc_info:
        convert2fasta(None, 3, 1)
    assert exc_info.value.args[0] == 'sequence is not a string.'

    with pytest.raises(AssertionError) as exc_info:
        convert2fasta(['A', 'T', 'C', 'G', 'A'], 3, 1)
    assert exc_info.value.args[0] == 'sequence is not a string.'