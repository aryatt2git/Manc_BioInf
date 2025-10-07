import pytest
from modules.chunk_sequence import chunk_sequence
#from utilities.pytest_checks import test_other_data_types

@pytest.mark.parametrize('sequence, chunk_length, expected', [
        ('ATCGGCTA', 3, 'ATC GGC TA'),                                                   # checks normal function
        ('atcggcta', 3, 'ATC GGC TA'),                                                   # maybe function converts to uppercase
        ('ATBXZ', 2, 'B at position 3 in the sequence is not a nucleotide.'),            # depends on how invalid chars handled
        ('', 3, ''),                                                                     # empty input returns empty list
        ('ATCG', 10, 'ATCG'),                                                            # chunk size > seq length
        ('ATCG', 4, 'ATCG'),                                                             # chunk size == seq length
        ('ATCG', 1, 'A T C G'),                                                          # chunk size = 1
])

def test_chunk_sequence(sequence, chunk_length, expected):

    with pytest.raises(AssertionError) as exc_info:

        chunk_sequence(sequence, chunk_length)

    assert str(exc_info.value) == expected

    output = chunk_sequence(sequence, chunk_length)

    assert output == expected

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
    with pytest.raises(TypeError):
        chunk_sequence(12345, 3)
    with pytest.raises(TypeError):
        chunk_sequence(None, 3)
    with pytest.raises(TypeError):
        chunk_sequence(['A', 'T'], 3)