import pytest
from modules.DNA2Prot import DNA2Prot

def test_DNA2Prot():

    sequence = 'aggagtaagcccttfgcaactggaaatacacccattg'

    DNA2Prot(sequence)

    assert type(sequence) == str

    for n in sequence:
        assert n in ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']
