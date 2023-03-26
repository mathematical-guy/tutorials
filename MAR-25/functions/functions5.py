# One liner functions

"""
    Lambda function (Anonymous function) are one liner functions
    lambda is a keyword
    syntax for lambda function:
        lambda arguments: return logic
    but since lambda function has no name. so we have to give it name
    f = lambda arguments: return logic
    e.g 
    f = lambda x: x*x
    
"""

def calculate_square(x):
    """
        This function does 
         - takes integer input from user
         - prints out the square of the input number
    """
    print("Square of X is", x*x)


my_func = lambda : True
my_func2 = lambda x, y, z: x + y + z


print(my_func2(1, 2, 5))