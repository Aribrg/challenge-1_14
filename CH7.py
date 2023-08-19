## CH7: Compound Interest

def get_p():
    p = float(input('Enter principal amount that was originally deposited into the account: '))
    return p

def get_r():
    r = float(input('Enter the annual interest rate: '))
    return r

def get_num():
    num = int(input('Enter the number of times per year that the interest is compounded: '))
    return num

def check_number():
    number = get_num()
    if number >= 1 and number <= 12 :
        n = number
    else:
        n = int(input('enter a numbre between 1 and 12: '))

check_number()   



def years ():

    t = int(input('Enter the specified number of years: '))
    return t

def multi():
    p = get_p()
    r = get_r()
    n = get_num()
    t = years()
    A = float ( p * (1 + r / n ) ** n * t)
    return A

def show():

    res = multi()
    print(f'the amount of money in the account after the specified number of years is:', res)

show()





