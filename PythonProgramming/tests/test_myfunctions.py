import pytest
from modules.chunk_sequence import chunk_sequence

def test_chunk_sequence():

    chunk_sequence('aggagtaagcccttgcaactggaaatacacccattg', 3)