k=0
while(True):
    ans=input()
    if ans =="Да" :
       print("Это отлично")
       break
    else:
       k+=1
       if (k>=5):
          print("Это безнадежно")
          break
       print("Увы, это неправильный ответ")
