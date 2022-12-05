class Rucksack:

    def __init__(self, contents):
        self.contents = contents
        # On initialise, split the contents to compartment 1 and 2
        self.compartment = self.compartmentalise(contents)

    def compartmentalise(self, contents):
        middle = int(len(contents)/2)
        sliced = [contents[:middle], contents[middle:]]
        return sliced
        
    # Find the item type that appears in both compartments of each rucksack
    def get_common_item(self):
        for i in self.compartment[0]:
            try:
                if i in self.compartment[1]:
                    return i
            except:
                print("Something went wrong.")
