#Python code to explain defining
#and using class

#A class named python_program is defined
class first_program:
    '''
    This program has two methods: hi and hi_again
    '''
    greeting = 'Hello Everybody\n' #Class variable definition

    #Now we define two instances of this class as "hi" and "hi_again"
    def hi(self):
        greet = 'Hello World!\n'
        print(greet)
    def hi_again(self):
        greet_again = 'Hello again!\n'
        print(greet_again)

#Procedures to call the class

x = first_program() # Calling the class
print('The type of object storing class calling is:', type(x))
x.hi() #Calling an instance of "x" class
x.hi_again() # Calling another instance of "x" class
# Results of both instances depend on thier definitions

#Acessing class variable
#Class variable can be accessed from anywhere
print(first_program.greeting)

#Printing the documentation string
print(first_program.__doc__)
