def my_film (my_fav_film):
    print (f"My favorit falm is {my_fav_film}")

def my_film (" 'The Lord of the Rings' ")


def make_country (name, country ):
    info_ = {'name': name, 'country': country}
    return info_
country_ = make_country ('Kyiv', 'Ukraine')
print (country_)




def make_operation ( a , b = None, *args):
    if a == "+":
        summ = 0
        for x in args: 
           summ += x 
        print (summ)
            
    if a == "-":
        summ1 = b
        
        for e  in args:
            summ1 = summ1  - e 
            

        
            
        print (summ1)

    if a == "*":
        summ2 = 1
        for g in args: 
           summ2 *= g
        print (summ2)

    

make_operation ("-", 5, 5, -10, -20 )
make_operation ("+", 1, 2, 2, 3, 4 )
make_operation ("*", 10, 4, 10 )


 
    
    


