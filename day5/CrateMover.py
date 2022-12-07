class CrateMover9k:

    def __init__(self, map):
        self.MAP = map     # Stores the translated cargo map

    def showCargo(self):
        print("\nThe Cargo currently looks like this:")
        for index, stack in enumerate(self.MAP):
            print(index + 1, stack)
        print("\n")

    def moveCargo(self, instruction):
        qty = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]
        print(f"=== Moving {qty} cargo from Stack {from_stack} to Stack {to_stack} ===")
        for i in range(qty):
            self.MAP[to_stack - 1].append(self.MAP[from_stack - 1].pop())
        
    def showTopOfEachStack(self):
        for index, stack in enumerate(self.MAP):
            print(index + 1, stack[-1])

class CrateMover9k1(CrateMover9k):

    def __init__(self, map):
        super().__init__(map)

    def moveCargo(self, instruction):
        qty = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]
        print(f"=== Moving {qty} cargo from Stack {from_stack} to Stack {to_stack} ===")
        temp = []
        for i in range(qty):
            temp.append(self.MAP[from_stack - 1].pop())
        temp = list(reversed(temp))
        self.MAP[to_stack - 1] += temp