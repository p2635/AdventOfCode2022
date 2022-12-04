"""Module providing tests for Advent of Code Day 2."""

# -----------------------------------------------
# Imports
# -----------------------------------------------

import pytest
from day2.day2 import *

# -----------------------------------------------
# Tests
# -----------------------------------------------

@pytest.mark.parametrize("gesture", ["A", "X"])
def test_get_gesture_rock(gesture):
    assert get_gesture(gesture) == "Rock"

@pytest.mark.parametrize("gesture", ["B", "Y"])
def test_get_gesture_paper(gesture):
    assert get_gesture(gesture) == "Paper"

@pytest.mark.parametrize("gesture", ["C", "Z"])
def test_get_gesture_scissors(gesture):
    assert get_gesture(gesture) == "Scissors"

gesture_scores = [
    ("Rock", 1),
    ("Paper", 2),
    ("Scissors", 3),
]
@pytest.mark.parametrize('gesture, score', gesture_scores)
def test_get_gesture_score(gesture, score):
    assert get_gesture_score(gesture) == score
