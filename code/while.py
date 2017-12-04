# Program demonstrating usage of while loop

# Program to count number of steps and time taken for thier execution

import time #This module is used for timing lines of codes
import numpy as np

i = 0 # initializing the counter
while(i<10): # counter condition
    start = time.clock() # defining the variable which stores time.clock(value)
    print("Square root of %d  = %3.2f:"%(i,np.sqrt(i))) # printing the number and its squareroot
    i=i+1 # incrementing the counter
    timing = time.clock() - start # prints time taken to execute two lines of code above
    print("Time taken for execution = %e seconds \n" % timing)
    
print("The end") # signifies exiting the loop after condition is satisfied