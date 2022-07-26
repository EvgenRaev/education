
text_inp = input().split() 

d = dict()
 
for word in text_inp:
        
    if word in d:  
        d[word] = d[word] + 1
    else:           
        d[word] = 1

print (d)
