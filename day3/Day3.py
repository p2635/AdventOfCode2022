from Rucksack import *
from RucksackAnalyser import *

newSack = Rucksack("Stuff")

print(get_item_type("h"))

newSack.one_more_big_item()
newSack.one_more_big_item()
newSack.one_more_big_item()
newSack.one_more_big_item()
print(newSack.big)

newSack.one_more_small_item()
print(newSack.small)

print(newSack.get_total_item_count())

print(get_item_priority("c"))