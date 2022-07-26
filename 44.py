#Перше завдання
first='Ле'

if len(first) >= 2:
    print(first[0:2] + first[-2:])
elif len(first) == 2: 
    print (first + first)
else: 
    print (' ')

#Скрипт для одного телефонного номера

tel_number = '1111111a111'


if len(str(tel_number))==10 and type(tel_number) == int  :
    print('Номер телефону відповідає стандарту', end=' \n\n')

else: 
    print ('Номер телефону не відповідає стандарту:', tel_number, end=' \n\n')


#Скрипт для списку із телефонних номерів

tel_numbers = [7811111111, 9222222229, 3333366, 444444444, 50111111111, 30111, 45, 25, 20]

for i in tel_numbers: 
    if len(str(i)) != 10 or type(i) != int : 
        print ("Даний номер телефону не відповідає стандарту:", i, end=' \n\n' ) 

#Завдання з правильною відповіддю

x_question=0
print ("Дайте відповіть на приклад 2+2=")
while(True):
    ans=input()
    if ans == "4" :
       print("Вітаємо, правильна відповідь")
       break
    else:
       x_question += 1
       if ( x_question >= 5):
          print("Вчіть матетатику")
          break
       print("Нажаль відповідь не правильна")

#Завдання на введення ім'я

my_name_1 = 'Evgen'
my_name = input('Введіть Ваше імя:  ') 

if  my_name == my_name_1.lower() or my_name == my_name_1 :
   print("Yes!")
else :
    print("No(")






    