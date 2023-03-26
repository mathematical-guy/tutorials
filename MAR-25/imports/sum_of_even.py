from even import get_even_number_upto_n      # part of code
import myfolder.helloworld 
# import even           # All code

def sum_even(numbers):
    total = sum(numbers)
    return total


n = 14
numbers = get_even_number_upto_n(14)
print(numbers)
total = sum_even(numbers)
print(total)