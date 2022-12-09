"""Module providing tests for Advent of Code Day 7."""

# -----------------------------------------------
# Imports
# -----------------------------------------------

from day7.Items import Folder
from day7.Navigator import Navigator
from day7 import Parser

# -----------------------------------------------
# Fixtures - THIS DOESN'T WORK
# -----------------------------------------------

# @pytest.fixture
# def set_root_folder():
#     root_folder = Folder("/")
#     global navi = Navigator(root_folder)

# -----------------------------------------------
# Tests
# -----------------------------------------------

def test_is_file():
    string = "24836 rsjcg.lrh"
    assert Parser.parse_command(string)

def test_many_navi_functions():

    root_folder = Folder("/")
    navi = Navigator(root_folder)

    print("Current directory is", navi.pwd())

    navi.add_folder("NewFolder")
    navi.add_file("NewFile", 1024)
    navi.add_folder("NewFolder2")

    print(navi.list_items())

    navi.go_down_a_folder("NewFolder")
    print("Current directory is", navi.pwd())

    navi.go_up_a_folder()
    print("Current directory is", navi.pwd())

    assert navi.pwd() == "/"

def test_get_file_size_one_file():

    root_folder = Folder("/")
    navi = Navigator(root_folder)

    navi.add_file("NewFile", 1024)
    assert navi.get_current_folder_size() == 1024

def test_get_file_size_three_files():

    root_folder = Folder("/")
    navi = Navigator(root_folder)
    for i in range(3):
        navi.add_file(f"NewFile{i}", 1024)
    assert navi.get_current_folder_size() == 1024 * 3

def test_get_file_size_in_subfolder():

    # Arrange
    root_folder = Folder("/")
    navi = Navigator(root_folder)

    # Act
    navi.add_folder("Subfolder1")
    navi.go_down_a_folder("Subfolder1")
    navi.add_file("TestFile1", 1024)
    navi.go_up_a_folder()

    # Assert
    assert navi.get_current_folder_size() == 1024

def test_get_file_size_in_subfolder2():

    # Arrange
    root_folder = Folder("/")
    navi = Navigator(root_folder)

    # Act
    navi.add_folder("Subfolder1")
    navi.add_file("TestFile1", 1024)

    navi.go_down_a_folder("Subfolder1")
    navi.add_file("TestFile2", 1024)
    navi.go_up_a_folder()

    # Assert
    assert navi.get_current_folder_size() == 2048

# Not a true unit test, verify with eyes
def test_print_current_dir_file_size():

    # Arrange
    root_folder = Folder("/")
    navi = Navigator(root_folder)

    # Act
    navi.add_folder("Subfolder1")
    navi.add_file("TestFile1", 1024)

    navi.go_down_a_folder("Subfolder1")
    navi.add_file("TestFile2", 1024)
    navi.go_up_a_folder()

    # Assert
    # navi.print_size_include_subfolders()
