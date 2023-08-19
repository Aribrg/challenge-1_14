

def get_value1():
    
    number_kilometer = float(input('Enter the number of kilometer: '))
    return number_kilometer

def get_value2():

    liter_gas = int(input('Enter the liter of gas used: '))
    return liter_gas

def multi():   
    a=get_value1() 
    b=get_value2()
    KPL = a / b
    return KPL

def show():
    kpl = multi()    
    print(f'KPL value is:',kpl)

show()