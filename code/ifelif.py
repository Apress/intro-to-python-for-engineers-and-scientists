# Program to calculate shipping cost based on money spent and location

total = int(input('What is the total amount for your online shopping?\n'))
area = input('''Type "I" if you are shopping within India...
and "O" if you are shopping outside India\n''')

if area == "I":
    if total <= 500:
        print("Shipping Costs INR 20.00")
    elif total <= 1000:
            print("Shipping Costs INR 100.00")
    elif total <= 1500:
            print("Shipping Costs INR 250.00")
    else:
        print("FREE")

if area == "O":
    if total <= 500:
        print("Shipping Costs INR 75.00")
    elif total <= 1000:
        print("Shipping Costs INR 200.00")
    elif total <= 1500:
        print("Shipping Costs INR 500.00")
    else:
        print("FREE")