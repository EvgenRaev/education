name='Evgen'
day='24.06.2022'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

s='Good day {}! {} is a perfect day to learn some python.'
print(s.format(name, day) , end =' \n\n\n')

last='Raiev'
print(name + ' ' + last, end =' \n\n\n') 

a=5
b=2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(float(a % b))
print(a ** b)
print(a // b , end =' \n\n\n')


name = 'Dostoyevsky'
lenght_of_name = len(name)
print(len(name) == 11)