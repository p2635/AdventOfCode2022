--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

# Planning it out

what is the cargo table telling me? What info can I gather?

- The number of stacks = 9, I know this because...
        - I can get this information by reading the bottom line
        - I can also get this information by counting cargo items
- Cargo is in the format [(Capital letter)]
- Empty cargo is in the format of 3 whitespaces.
- The gaps between the cargo is 1 whitespace.

Bonus stuff
- Cargo stack size has no defined limit (Y axis) - I can assume this is 9 (blocks) to make things easier
- Number of cargo stacks has no defined limit (X axis)  - I can assume this is 8 (blocks) to make things easier

Other
- I need to investigate what methods can help me here, specifically translating the cargo map to something that python understands. Something like this maybe? https://note.nkmk.me/en/python-list-transpose/

# What I learned

- To import from another folder, do this: `from (foldername).(module) import (function)`. The real life context is pytest, `from day5.Day5 import hello`.
- I learned that the '-' is an invalid character for import, so don't name your files something like `hello-there`.
- I managed to fix the pytests!
- The asterisk unpacks an iterable. If you have something like [[1,2,3], [2,3,4]] and you want to pass this into a function; you can pass it in by doing this `a = [[1,2,3], [2,3,4]]` then `zip(*a)`.
- Repack to a list of lists, since zip returns a list of tuples https://stackoverflow.com/a/6473724
- Extract digits with regex (part 2 of this article): https://www.askpython.com/python/string/extract-digits-from-python-string
- Estimated time spent 10-12 hours (part 1)

# Part 2

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

# What I learned

- To read later, https://mathspp.com/blog/pydonts/pass-by-value-reference-and-assignment. I feel like I was messing with the same variable all along and pointers were going to the same place. Need to revise on this one. For now I will fudge it, have a look at how you implemented parsedmap1 and parsedmap2.
- Don't forget you can combine lists by just using an addition + operator, no need to do fancy append stuff. That just complicated things.
- reversed() returns an iterator object, not a reversed list. You still need to do something like list(reversed(x)) to get it back into the form that you wanted.