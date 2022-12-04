class Rucksack:

    def __init__(self, contents):
        self.contents = contents
        self.big = 0
        self.small = 0
        # On initialise, split the contents to compartment 1 and 2
        self.compartment = [0, 1] # to be implemented

    def get_total_item_count(self):
        count = self.big + self.small
        return count

    def one_more_big_item(self):
        self.big += 1
    
    def one_more_small_item(self):
        self.small += 1
        