
def  vegetrian():
    print('if you are a vegetrian person pleas type yes but if you are not a vegetrian person type no')
    vegetrian_person =input('enter yes or no :')
    return vegetrian_person

def vegan():
    print('if you are a vegan person pleas type yes but if you are not a vegan person type no')
    vegan_person =input('enter yes or no :') 
    return vegan_person

def gluten_free():
    print('if you are a gluten free pleas type yes but if you are not a gluten free type no')
    gluten_free_person =input('enter yes or no :') 
    return gluten_free_person


def choice_restuarant():
    a=vegetrian()
    b=vegan()
    c=gluten_free()

    if a == 'yes' and b =='yes' and c =='yes':
        print('Here are your restaurant choices:Corner Café and The Chef’s Kitchen')

    elif a == 'yes' and b =='no' and c =='yes':
        print('Here are your restaurant choices:Main Street Pizza Company')


    elif a == 'yes' and b =='no' and c =='no':
        print('Here are your restaurant choices:Mama’s Fine Italian')


    elif a == 'no' and b =='no' and c =='no':
        print('Here are your restaurant choices:Joe’s Gourmet Burgers')   
   

    else:
        print('sorry we do not any offer for you')   
choice_restuarant()

print('welcome')     