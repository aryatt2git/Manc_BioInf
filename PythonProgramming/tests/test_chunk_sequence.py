import pytest
from modules.chunk_sequence import chunk_sequence

def test_chunk_sequence():

    sequence = 'aggagtaagcccttgcaactggaaatacacccattg'

    chunk_length = 3

    chunk_sequence(sequence, chunk_length)

    assert type(sequence) == str

    for n in sequence:
        assert n in ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']

    assert (type(chunk_length) == int)

    assert len(sequence) % chunk_length == 0