## CH9: Quarter of the Year

def get_value():
    a = int(input('Enter a number of months between 1 to 12:'))
    return a

def season():
    number = get_value()
    if number >= 1 and number <= 3:
       print('The month is in the first quarter')

    elif number >= 4 and number <= 6:
       print('The month is in the second quarter') 

    elif number >= 7 and number <= 9:
        print('The month is in the third quarter')      

    elif number >= 10 and number <= 12:
        print('The months is in the fourth quarter')

    else:
        print('It is not correct please enter another number')  

season()
               
    