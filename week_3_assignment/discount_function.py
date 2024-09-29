def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price - ((discount_percent / 100) * price)
        return price
    else:
        return price
    
print(calculate_discount(int(input('Enter original price of item ')), int(input('Enter discount percentage '))))