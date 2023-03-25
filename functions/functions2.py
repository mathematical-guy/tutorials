# PROGRAM to discuss how to use parameters  ?

def calculate_total_price(table_count, chair_count):
    """
        Price for one Table: 500 
        Price for one Chair: 300
        Function calculates the total price for purchase of 
        multiple chair and tables
    """
    total = 500*table_count + chair_count*300
    print("Total: ", total)


# Non Positional Arguments
calculate_total_price(chair_count=3, table_count=5)     


# Positional Arguments (order matters) (order of 5 and 3 matters)
calculate_total_price(5, 3)                             
                                                        