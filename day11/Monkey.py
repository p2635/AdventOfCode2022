class Monkey:

    def __init__(self, items,  operation, test, m1, m2):
        self.items = items
        self.operation = operation
        self.divi_test = test # Assume it's only division
        self.target_monkey1 = m1
        self.target_monkey2 = m2
        self.inspect_count = 0

    def inspect(self, item):
        item = eval(self.operation)
        return item

    def throw_first_item(self, Monkey):
        Monkey.items.append(self.items[0])
        self.items.pop(0)
        return True

    def get_bored(self, item, divide_by):
        item = int(item / divide_by)
        return item

    def divitest_item(self, item):
        return item % self.divi_test == 0
