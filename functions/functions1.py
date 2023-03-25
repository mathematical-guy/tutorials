

"""
    What are functions ?
     Functions are part of code, which only runs when it is required.
     When the logic is required to be executed, function calling is done
     function calling means using the function
"""

def calculate_square():
    """
        This function does 
         - takes integer input from user
         - prints out the square of the input number
    """
    x = int(input("Enter number: "))
    print("Square of X is", x*x)


def calculuate_simple_interest():
    """
        This function does:
        -takes input of Principal amount and Time period in integer
        -prints simple intrest p*r*n/100
    """
    p = int(input("Enter Principal Amount: "))
    n = int(input("Enter Number of months (time period): "))

    r = 2.5
    simple_interest = (p*n*r)/100
    print("Your simple interest is", simple_interest)


print("Hello World")


"""
    Function is only executed when it is called. 
    If it is not called, it is ignored
"""
calculate_square()
calculuate_simple_interest()