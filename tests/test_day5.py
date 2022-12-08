"""Module providing tests for Advent of Code Day 5."""

# -----------------------------------------------
# Imports
# -----------------------------------------------

import pytest
from day5 import TextFileParser

# -----------------------------------------------
# Fixtures - THIS DOESN'T WORK
# -----------------------------------------------

# @pytest.fixture
# def parser():
#     return CargoParser()

# -----------------------------------------------
# Tests
# -----------------------------------------------

# This test will check class variables are accessible
def test_check_cargo_class_vars():
    assert TextFileParser.GAP == 1 and TextFileParser.LENGTH == 3

# This test will take in a line and check how many stacks exist
# based on blank spaces
row_data = [
    ("", 0),
    ("        ", 3)
]
@pytest.mark.parametrize("row, count", row_data)
def test_check_cargo_count(row, count):
    assert TextFileParser.check_cargo_count(row) == count

# This test will take in a line and convert it
# to a list like ["S", "", "", "", "M" ...]
row_data = [
    ("[S]             [M] [C] [T] [F] [B]", ["S", " ", " ", " ", "M", "C", "T", "F", "B"]),
    ("[N] [T] [R] [T] [T] [T] [M] [M] [G]", ["N", "T", "R", "T", "T", "T", "M", "M", "G"]),
    ("[Z] [G] [V] [V] [Q] [M] [L] [N] [R]", ["Z", "G", "V", "V", "Q", "M", "L", "N", "R"])
]
@pytest.mark.parametrize("row, lst", row_data)
def test_line_to_list(row, lst):
    assert TextFileParser.line_to_list(row) == lst
