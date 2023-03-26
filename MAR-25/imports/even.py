

def get_even_number_upto_n(n):
    even_numbers = []
    for i in range(0, n+1):
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers



def get_odd_number_upto_n(n):
    odd_numbers = []
    for i in range(0, n+1):
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers
    

x = 3