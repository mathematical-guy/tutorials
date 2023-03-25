"""
    Suppose we have a list [23, 45, 100, 21, 67, 90] and 
    we have to total it's value

    # Pythonic Way (not our custom logic)
    l = [23, 45, 100, 21, 67, 90, 80, 120, 70, 23]
    total = sum(l)

    print(total)
    * (star) operator opens the list/tuple/set
    so *mylist means it opens (unfold) all the elements present in list
"""

def total_sum(*my_list):
    # If the number of arguments got higher, it is difficult to manage for e.g
    # total =  a + b + c + d + e + f + g + h + aa + ba + ce
    # return total
    # So it is required to open (unfold) list of variables and then use it
    # Unfold is done by using * operator
    my_total = 0
    for number in my_list:
        my_total = my_total + number
    
    return my_total



mysum = total_sum(1, 2, 3, 5, 6, 80, 114, 5)
print(mysum)