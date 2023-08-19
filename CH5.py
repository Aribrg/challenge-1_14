

n = int(input('How many cookies you want to make? '))


def suger_cookie():

    SUGAR = 1.5 / 48
    s = SUGAR * n
    return s

def show_suger():
    S = suger_cookie()
    print (f' sugar is {S: .2f}')
    

def  butter_cookie ():
    BUTTER = 1 / 48
    x = BUTTER * n
    return x

def show_butter():
    X =butter_cookie()
    print (f' sugar is {X: .2f}')

def floar_cookie():

    FLOAR = 2.75 / 48
    y = FLOAR * n
    return y

def show_floar():
    Y = floar_cookie()
    print (f' sugar is {Y: .2f}')


show_suger()
show_butter()
show_floar()
