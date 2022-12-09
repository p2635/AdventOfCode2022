class Item:

    def __init__(self, name, parent_folder = None, size = 0):
        self.name = name
        self.parent_folder = parent_folder
        self.size = size

class Folder(Item):

    def __init__(self, name, parent_folder = None):
        Item.__init__(self, name, parent_folder)
        self.contents = []

    def get_size(self):
        
        total_size = 0

        for i in self.contents:    
            total_size += i.get_size()

        self.size = total_size
        return total_size

    def print_size_recursive(self):

        print(f"=== Folder {self.name} ===")
        print(f"=== (size = {self.get_size()}) ===")

        for i in self.contents:
            print(i.name, i.get_size(), f"Parent = {i.parent_folder.name}")
            if isinstance(i, Folder):
                i.print_size_recursive()

class File(Item):

    def __init__(self, name, parent_folder = None, size = 0):
        Item.__init__(self, name, parent_folder, size)
 
    def get_size(self):
        return self.size
