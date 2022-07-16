# гра
import random
attempt = 0
comp_val = random.randint (1, 10)
print ('Вгадай число від 1 до 10ти')

for i in range(1, 4):
    attempt = int(input('Спробуй вгадати: '))
    if attempt != comp_val :
        print ('Спробуй ще')
        attempt += 1
    elif attempt == comp_val :
        print ('Вітаю, ти вгадав')  
        break 
    else: 
        break
if attempt > 3 : 
    print ('Число, яке загадав компьютер -', comp_val)    
         
# день народження
import datetime
name = "Evgen"

my_birth_day = datetime.date (1982, 7, 25)
today = datetime.date.today()
age = today.year - my_birth_day.year - 1
next_years = age + 1 

print(f"Hello  {name}! on your next birthday you’ll be {next_years} years.")


#Рандомні слова

import random

text = 'hello'


for i in range (5) :
    random_index = random.sample(text, 5)
    random_index_ = ''.join(random_index)

    print(random_index_, end=" , ")