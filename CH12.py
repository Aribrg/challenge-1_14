### CH12: Population



def table():
   print('DAY  '          '  Approximate Population')

def data():
   num = 2
   table()
   for i in range(1,11):
     
     num = (0.3 * num + num)
     
     print(f'{i}\t\t {num}')
    

data()