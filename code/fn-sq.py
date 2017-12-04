def square(x):
    '''
    square() squares the input value
    One must only used numeric data types
    to avoid getting error
    '''
    return x*x

for i in range(10):
    squared_i= square(i)
    print(i, squared_i)
