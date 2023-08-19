### CH6: Stock Transaction Program

stock = 2000
buy_stock = 40
sell_stock = 42.75


def buy():
    total_buy_stock = stock * buy_stock
    return total_buy_stock

def sell():
    total_sell_stock =  stock * sell_stock
    return total_sell_stock

def commission_buy():
    a = buy()
    x = (a * 3) / 100
    return x

def commission_sell():
    b = sell()
    x = (b * 3) / 100
    return x

def show_info():
    b = buy()
    s = sell()
    cb =commission_buy()
    cs =commission_sell()
    print(f'The total amount paid for the purchase of shares:',b)
    print(f'The total amount received for the sale of shares:',s)
    print(f'Commission from the purchase of shares:',cb)
    print(f'Commission from the sale of shares:',cs)


def sood():
    a = buy()
    b = commission_buy()
    s = a - b
    return s

def zarar():
    a = sell()
    b = commission_sell()
    s = a - b
    return s

X = sood()
Y = zarar()


if X <= 0 :
    print('You lost when buying stocks')
  
else:
    print('You made a profit when buying stocks') 


if Y <= 0 :
    print('You lost when selling stocks')       
else:
    print('You made a profit when selling stocks') 