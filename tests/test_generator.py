"""
    Testing for sfcpy.Generator
"""
import os
import pytest
from sfcpy.generator import hc_generator, hc_builder, split_seq


# test hc_generator
def test_hc_generator():
    tape = hc_generator(['odru'], 3, 'test_table.txt')
    expected = "Order 2\nodrurrdldrdlluld\nOrder 3\nodrurrdldrdllulddrdlddrurdruulurrrdlddrurdruuluruuldllurulurrdru\n"
    with open('test_table.txt', 'r') as file:
        test_tape = ""
        for line in file.readlines():
            test_tape = ''.join([test_tape, line])
        assert test_tape == expected

    os.remove('test_table.txt')
