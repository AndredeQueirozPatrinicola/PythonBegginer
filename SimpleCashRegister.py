print('Welcome to the grocery store')

start = input("Let's start some shopping? [Yes] [No]: ")

print("Type 0 to end the shopping")

while start == 'Yes' or start == 'yes' or start == "y" or start == "Y":

    count = 1
    price = float(input(f"Product price {count}: $ "))
    total = 0
    price_1 = price
    while price > 0:
        count += 1
        price = float(input(f"Product price {count}: $ "))
        total = total + price + ((price_1/2)*2)

    else:
        print(f'Total: $ {total}')
    
    cash = int(input("Cash: $ "))
    change = cash - total

    print(f"Change: $ {change:.2f}")
    
    start = input("Another one? [Yes] [No]: ")

else:
    print('Ok!Bye!')
