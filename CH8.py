## CH8: Number Analyzer

def get_num():

    Num = int(input('Enter a number please: '))
    return Num

def type_num():
     a = get_num()
     if (a % 2 == 1):
        print('The number is an odd number')

     else:
        print('The number is an even number')
     x = a
     return a   
        
def num_range():
    
    b = type_num()

 
    if b > 0:
        print('The number is positive')

    elif b ==0 : 
        print('The number is zerro') 

    else:
        print('The number is negetive')      
        
        
num_range()        







    
     
