import pytest
from modules.chunk_sequence import chunk_sequence
#from utilities.pytest_checks import test_other_data_types

@pytest.mark.parametrize('sequence, chunk_length, expected', [
        ('ATCGGCTA', 3, 'ATC GGC TA'),      # checks normal function
        ('atcggcta', 3, 'ATC GGC TA'),      # maybe function converts to uppercase
        ('ATBXZ', 2, 'AT BX Z'),            # depends on how invalid chars handled
        ('', 3, ''),                        # empty input returns empty list
        ('ATCG', 10, 'ATCG'),               # chunk size > seq length
        ('ATCG', 4, 'ATCG'),                # chunk size == seq length
        ('ATCG', 1, 'A T C G'),             # chunk size = 1
])

def test_chunk_sequence(sequence, chunk_length, expected):

    output = chunk_sequence(sequence, chunk_length)

    assert output == expected

    assert type(sequence) == str

    for n in sequence:
        assert n in ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']

    assert (type(chunk_length) == int)

def test_chunk_length():
    with pytest.raises(ValueError):
        chunk_sequence('ATCG', 0)
    with pytest.raises(ValueError):
        chunk_sequence('ATCG', 0-1)

def test_other_data_types():
    with pytest.raises(TypeError):
        chunk_sequence(12345, 3)
    with pytest.raises(TypeError):
        chunk_sequence(None, 3)
    with pytest.raises(TypeError):
        chunk_sequence(['A', 'T'], 3)