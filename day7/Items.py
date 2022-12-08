class Item:

    def __init__(self, name, parent_folder = None):
        self.name = name
        self.parent_folder = parent_folder

class Folder(Item):

    def __init__(self, name, parent_folder = None):
        Item.__init__(self, name, parent_folder)
        self.contents = []

    def get_size(self):
        size = 0
        for i in self.contents:
            print(i.name, i.getsize())
            size += i.get_size()
        return size
        # sum of all files, or zero if no files, recursive?

class File(Item):

    def __init__(self, name, parent_folder = None, size = 0):
        Item.__init__(self, name, parent_folder)
        self.size = size

    def get_size(self):
        return self.size
