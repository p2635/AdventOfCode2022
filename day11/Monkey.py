class Monkey:

    def __init__(self, items = [],  operation = "* 11", test = 23):
        self.items = items
        self.operation = operation
        self.test = test # Assume it's only divisible by
        self.inspect_count = 0

    def inspect(self, item):
        print(f"\tMonkey inspects item with worry level {item}.")
        item = eval("item " + self.operation)
        print(f"\t\tWorry level is {self.operation} to {item}.")
        item = self.get_bored(item)
        self.inspect_count += 1
        return item
    
    def inspect_items(self):
        for item in self.items:
            self.inspect(item)

    def throw_last_item(self, Monkey):
        Monkey.items.append(self.items[-1])
        print(f"\t\tItem with worry level {item} is thrown to a monkey.")
        self.items.pop()
        return True

    def get_bored(self, item):
        item = int(item / 3)
        print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {item}.")
        return item

    def test(self, item):

        if item % self.test == 0:
            # self.throw(Monkey)
            pass
        else:
            # self.throw(other monkey)
            pass
