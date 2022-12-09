from Items import File, Folder

class Navigator:

    def __init__(self, folder):
        self.active_folder = folder

    def pwd(self):
        return self.active_folder.name

    def go_up_to_root(self):
        print("Currently at \ directory")
        while self.active_folder.name != "/":
            self.go_up_a_folder()
        return True

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

    def add_folder(self, name):
        new_folder = Folder(name, self.active_folder)
        self.active_folder.contents.append(new_folder)

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
    def print_directory_structure(self, folder, indent=0):
        # Iterate over the folders and files in the 'contents' attribute
        for item in folder.contents:
            # Print the name of the item, indented by the specified amount
            print(" " * indent + item.name)
            # Check if the item is a folder
            if isinstance(item, Folder):
                # If it is a folder, recursively call the function to print its contents
                self.print_directory_structure(item, indent + 2)

    # Try and add up all the 100000 bytes of folders together
    # Work in progress, I give up, spent hours. Easy to give up.
    def report_on_part1(self, folder, limit = 100000):

        total_size = 0

        for i in folder.contents:

            if isinstance(i, File):
                continue

            elif isinstance(i, Folder):
                if folder.size <= limit:
                    total_size += folder.size
                    total_size += self.report_on_part1(i)

        return total_size

