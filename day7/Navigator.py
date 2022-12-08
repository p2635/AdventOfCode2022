from Items import File, Folder

class Navigator:

    def __init__(self, folder):
        self.active_folder = folder

    def pwd(self):
        return self.active_folder.name

    def go_up_a_folder(self):
        self.active_folder = self.active_folder.parent_folder

    def go_down_a_folder(self, subfolder):
        self.active_folder = self.get_subfolder_by_name(subfolder)

    def get_subfolder_by_name(self, name):
        for folder in self.active_folder.contents:
            if folder.name == name:
                return folder

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
