# Program to generate even Pythagorean numbers
# Pythagorean numbers are those numbers for which pythagorus equation stands true 

from numpy import sqrt
n = input("Please input a maximum number:") # Asks user to input a number
n = int(n)+1 # converts the values stored in variable n to integer data type and adds 1 so that computation can be done if user feeds 0

# Two loops to define arrays for a and b for which c shall be computed
for a in range(1,n):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square)) # c is converted to an integer
        if ((c_square - c**2) == 0): # if square of a and square of b is equal to square of c then the result will be zero
            if (c%2 ==0): # checking if c is an even number
                print(a, b, c)