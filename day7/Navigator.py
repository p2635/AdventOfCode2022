from day7.Items import File, Folder

class Navigator:

    def __init__(self, root_folder):
        self.active_folder = root_folder
        self.root_folder = root_folder
        self.total_disk_space = 70000000
        self.required_update_space = 30000000

    def calc_unused_space(self):
        return self.total_disk_space - self.root_folder.size

    def is_enough_space(self):
        return self.calc_unused_space() > self.required_update_space

    def pwd(self):
        return self.active_folder.name

    def go_up_to_root(self):
        self.active_folder = self.root_folder

    def go_up_a_folder(self):
        self.active_folder = self.active_folder.parent_folder

    def go_down_a_folder(self, subfolder):
        self.active_folder = self.get_subfolder_by_name(subfolder)

    def get_subfolder_by_name(self, name):
        for folder in self.active_folder.contents:
            if folder.name == name and isinstance(folder, Folder):
                return folder
        return False

    def add_file(self, name, size):
        new_file = File(name, self.active_folder, size)
        self.active_folder.contents.append(new_file)
        return new_file

    def add_folder(self, name):
        new_folder = Folder(name, self.active_folder)
        self.active_folder.contents.append(new_folder)
        return new_folder

    def list_items(self):
        return [item.name for item in self.active_folder.contents]

    def get_current_folder_size(self):
        return self.active_folder.get_size()

    # Updates folder size attributes recursively
    def update_folder_sizes(self):
        for i in self.active_folder.contents:
            self.active_folder.get_size()
            if isinstance(i, Folder):
                self.active_folder = i
                self.update_folder_sizes()

    # print directory structure - credits to ChatGPT, not me
    def print_directory_structure(self, folder, indent = 0):
        # Iterate over the folders and files in the 'contents' attribute
        for item in folder.contents:
            # Get item type
            kind = type(item).__name__
            # Print the name of the item, indented by the specified amount
            print(" " * indent + kind + " " + item.name + f"({item.size})")
            # Check if the item is a folder
            if isinstance(item, Folder):
                # If it is a folder, recursively call the function to print its contents
                self.print_directory_structure(item, indent + 2)

    # Try and add up all the 100000 bytes of folders together
    def report_on_part1(self, folder, limit = 100000):

        total_size = 0

        for i in folder.contents:            
            if isinstance(i, Folder):
                if i.size <= limit and i.size > 0:
                    print(f"* This folder {i.name} has a size of {i.size}.")
                    total_size += i.size
                    print(f"The total size is {total_size}")
                total_size += self.report_on_part1(i)

        return total_size

    # Identify a folder that is >= a certain size limit
    def report_on_part2(self, folder, limit = 9192532):

        for i in folder.contents:            
            if isinstance(i, Folder):
                if i.size >= limit:
                    print(f"Folder {i.name} has size of {i.size}")
                    self.report_on_part2(i)
