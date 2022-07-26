

counts = dict()
words = input().split()

for word in words:
    if word in words:
        counts[word] += 1
    else:
         counts[word] = 1

print (counts)

    


    

   





    



