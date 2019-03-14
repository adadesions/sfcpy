"""
    Testing for sfcpy.Generator
"""

import pytest
from sfcpy.generator import hc_generator, hc_builder, split_seq


# test hc_generator
def test_hc_generator():
    tape = hc_generator(['odru'], 3, 'test_table.txt')

