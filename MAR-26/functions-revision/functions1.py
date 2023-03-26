
odd_number = []

def get_odd_numbers():
    number = 5
    for i in range(number):
        if i % 2 != 0:
            odd_number.append(i)



def `get_total`():
    total = 0
    for j in odd_number:
        total = total + j

    print(total)

print(odd_number)
get_odd_numbers()
get_total()

print(odd_number)