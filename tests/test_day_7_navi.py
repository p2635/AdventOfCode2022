"""Module providing tests for Advent of Code Day 7."""

# -----------------------------------------------
# Imports
# -----------------------------------------------

from day7.Navigator import Navigator
from day7.Item import Folder

# -----------------------------------------------
# Tests
# -----------------------------------------------

root_folder = Folder("/")
navi = Navigator(root_folder)

def test_many_navi_functions():

    print("Current directory is", navi.pwd())

    navi.add_folder("NewFolder")
    navi.add_file("NewFile")
    navi.add_folder("NewFolder2")

    print(navi.list_items())

    navi.go_down_a_folder("NewFolder")
    print("Current directory is", navi.pwd())

    navi.go_up_a_folder()
    print("Current directory is", navi.pwd())

    assert navi.pwd() == "/"
