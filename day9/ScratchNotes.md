# Head is directly above, below, left or right

To help me visualise:

0
1
2
 0 1 2

- (y, head high, tail low) 0 - 2 =  -2 comes out to be minus, so tail must go UP to catch up
- (y, head low, tail high) 2 - 0 = 0 comes out to be positive, so tail must go DOWN to catch up
- (x, head ahead of tail right) 2 - 0 =  2 comes out to be positive, so tail must go RIGHT to catch up
- (x, head ahead of tail right) 0 - 2 = -2 comes out to be negative, so tail must go LEFT to catch up

# Diagonals
up right (high)
up right (wide)
up left (high)
up left (wide)
down R (low)
down R (wide)
down L (low)
down R (wide)

# What I learned

* When debugging, print stuff out and see exactly where something failed. Compare the variable values.
* Check the logic in your functions, are they missing any scenarios?
* Don't be afraid to go and look for help, it's not a sign of weakness, you are stuck.
* If you are overwhelmed, really go take a break, you've been staring at the screen so long.
* Breaking it down and visualizing it helped a lot, rubber ducking your ideas.
* Making your code more generic (i.e. creating reusable functions) saves you time down the line.
* You can use breakpoints in VS code and watch certain vars, it helps you check what is going on.
