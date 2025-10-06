import pytest
from modules.DNA2Prot import DNA2Prot

@pytest.mark.parametrize('sequence, expected', [
        ('ATCGGC', 'IG'),                                     # checks normal function
        ('ATCGGCTA', 'IG-end of sequence out of frame'),      # end of DNA sequence out-of-frame
        ('atcggcta', 'IG-end of sequence out of frame'),      # maybe function converts to uppercase
        ('ATBXZ', 'Sequence could not be translated'),        # depends on how invalid chars handled
        ('', 'Input sequence was empty'),                     # empty input returns empty list
        ('AT', 'Sequence could not be translated'),           # DNA sequence length < codon length
        ('A T C G C T A G A T C G', 'IARS')                   # white spaces
])

def test_DNA2Prot(sequence, expected):

    output = DNA2Prot(sequence)

    assert output == expected

    assert type(sequence) == str

def test_other_data_types():
    with pytest.raises(AttributeError):
        DNA2Prot(12345)
    with pytest.raises(AttributeError):
        DNA2Prot(None)
    with pytest.raises(AttributeError):
        DNA2Prot(['A', 'T'])