### CH14: Printing Stars Pattern


def get_value():

   n = int(input('enter an even number'))
   row = int(n / 2)
   return row


def get_row():
    row=get_value()
    for i in range(0,row):
        for j in range(0,i+1):
            print('*',end=' ')
        print('\t') 
    row2 = row  
    return row2  


def get_row2():
    row2=get_row()       
    for i in range(row2+1,0,-1) :
        for j in range(0,i-1)  :
            print('*', end =' ') 
        print('\t') 


get_row2()           