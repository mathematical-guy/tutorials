"""
    Mutliple return values constructs a tuple and then returns it
"""

def calculate_total_price(table_count, chair_count):
    """
        Table: 500
        Chair: 300
    """
    total = 500*table_count + chair_count*300
    gst = 18
    return total, gst       # Example for multiple return values


def calculate_gst_include_price(price, gst):
    total = price*gst + price
    return total


def print_my_bill(number):
    print(number)


price, gst = calculate_total_price(chair_count=3, table_count=5)
new_price = calculate_gst_include_price(price, gst)
print_my_bill(new_price)