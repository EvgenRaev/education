try:
    def list1 (a,b,c):
        abc =  [a,b,c]
        return abc [5]
        
    aaa = list1 (1,2,3)
    print (type (aaa))
    print (aaa)

except IndexError:
    print ('Під таким індексом значення немає')

try:
    def dict1 (d,e,f):
        deff = {'d':1, 'e':2, 'f':3}
        return deff ['g']
    dict1 (4,4,5)
    bbb = dict1 (4,4,5)
    print (bbb)

except KeyError:
    print ('Такого ключа не існує')

try:
    def calc ():
        numb1 = int(input ("Введіть перше число "))
        numb2 = int(input ("Введіть друге число "))
        summ = numb1**2 / numb2
        return summ
    print (calc ())

except ValueError:
    print ('Введіть корректне значення')
except ZeroDivisionError:
    print ('Ділити на 0 не можна')




