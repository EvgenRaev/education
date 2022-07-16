import random
# Перший варіант першого завдання
my_randoms = [random.randint(1, 100) for i in range(10)]
max_number1 = max(my_randoms)

print (my_randoms)
print("Найбільше число:", max_number1)

# Другий варіант першого завдання
import random
my_random_list = [random.randint(1, 100) for i in range(10)]
new_random_list = []
index = 0
while index < len(my_random_list):
    element = my_random_list[index]
    if element ==  max(my_random_list):
        new_random_list.append(my_random_list[index])
    index += 1
print(my_random_list)
print("Найбільше число:", new_random_list)

#Друге завдання перший варіант

my_random_list_1 = [random.randint(1, 10) for i in range(10)]
my_random_list_2 = [random.randint(1, 10) for i in range(10)]
my_random_list_3 = []

index = 0
while index <= len(my_random_list_1):
    if index in my_random_list_1 and index not in my_random_list_2 :
        
            my_random_list_3.append(index)
    if index in my_random_list_2 and index not in my_random_list_1 :
            my_random_list_3.append(index)
    index += 1  
                 
print(my_random_list_1)
print(my_random_list_2)
print(my_random_list_3)

#Друге завдання другий варіант


my_randoms3 = []
for i in range (10):
    my_randoms3.append(random.randrange(1,101,1))


my_randoms4 = []
for i in range (10):
    my_randoms4.append(random.randrange(1,101,1))

my_randoms5=list(set(my_randoms3) ^ set(my_randoms4))
print (my_randoms5)


my_randoms5 = []

#Третє завдання, варіант перший

my_list = list(range(1, 101))

my_list_new = []

for i in my_list:
    if i  % 7 == 0 and i % 5 != 0 :
        my_list_new.append(i)

print(my_list_new)

#Третє завдання, варіант другий

my_list_ = list(range(1, 101))
my_list_new_ = []
ind = 0
while ind < len(my_list_):
    el = my_list_[ind]
    if el  % 7 == 0 and el % 5 != 0  :
        my_list_new_.append(el)
    ind +=1  
 
print(f"Всі числа, що є кратні 7, але не діляться на 5 {my_list_new_}")

