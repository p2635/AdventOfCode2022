# Inputs
The idea of cycles (ticks)
Command to add a value to x (called V)
Command to do nothing (noop)
x starts at 1.

# Ideas
* I need to be able to count cycles, I can use the concept of loops.
* addx V is two cycles, noop takes one cycle. That means I can use even and odd?

Maybe instead of trying to parse the text file and do random even and odd, I can create a list of commands that reflect the exact instruction of each cycle. For example.

1. noop read, do nothing
2. addx read, do nothing
3. addx now executes

In other words, I can create a more accurately command list that aligns with clock ticks.

No, the even and odd thing won't work because:
1. The clock always needs to keep ticking, one cycle at a time
2. You need to somehow use an iterator for this maybe? Delay the adding to x.

# Outputs
Signal strength (the cycle number multiplied by the value of the X register) 
Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
What is the sum of these six signal strengths?