class Item:

    def __init__(self, name, parent_folder = None):
        self.name = name
        self.parent_folder = parent_folder
        
        # information with directory structure? Should I just use lists of lists?

class Folder(Item):

    def __init__(self, name, parent_folder = None):
        Item.__init__(self, name, parent_folder)
        self.contents = []

    def get_size(self):
        pass
        # sum of all files, or zero if no files, recursive?

class File(Item):

    def __init__(self, name, parent_folder = None, size = 0):
        Item.__init__(self, name, parent_folder)
        self.size = size
