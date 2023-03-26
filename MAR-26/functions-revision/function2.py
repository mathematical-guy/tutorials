# Funtion
# Function declaration (definition)
# def withdraw_money(amount, gst):
#     print(amount)
#     print(gst)

# withdraw_money(10, 5000)
# withdraw_money(8000, 5)


# Function with default arguments 

# def withdraw_money(amount, gst=5):
#     print(amount)
#     print(gst)

# withdraw_money(5000, 10)
# withdraw_money(8000)

# Function with Non-positional arguments 

def withdraw_money(amount, gst):
    print(amount)
    print(gst)

withdraw_money(gst=10, amount=5000)
withdraw_money(8000)