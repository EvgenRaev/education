#Перше завдання

text_inp = input().split() 

d = dict()
 
for word in text_inp:
        
    if word in d:  
        d[word] = d[word] + 1
    else:           
        d[word] = 1

print (d)

# Друге завдання

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


total_price = 0

for key in stock.keys():
    total_price += stock[key] * prices[key]

print(total_price)


#третє завдання

tup1 = tuple (x for x in range(10))
tup2 = tuple (x**2 for x in range(10))
list1 = list [tup1,tup2 ]
print (tup1)
print (tup2)
print (list1)

list2 = list [ tuple(x for x in range(10)), tuple(x**2 for x in range(10)) ]
print (list2)

#четверте завдання

week1 =  [
    'Sunday', 'Monday ', 'Tuesday ', 'Wednesday ', 
    'Thursday ', 'Friday ', 'Saturday ',
]
enum1 = [1 , 2, 3, 4, 5, 6, 7]

week1_enum = dict (zip (week1, enum1))

week2 = dict.fromkeys (week1 )

week3 = dict (zip (enum1 , week1))


print(week1)
print(week2)
print(week1_enum)
print(week3)
