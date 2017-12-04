# Python code to demonstrate the concept
# of namespace and scope
i = 1

def my_function1():
    i = 2
    print("value of i in my_function()1 scope is", i )

def my_function2():
    i = 3
    print("value of i in my_function()2 scope is", i )

print('value of i in global scope is', i )
my_function1()
print('value of i in global scope is', i )
my_function2()
print('value of i in global scope is', i )