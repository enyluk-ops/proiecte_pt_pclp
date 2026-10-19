
import random
m=random.randint(1,20)
print('!!!WELCOME!!!')
n=0
incercari=0
while(n!=m):
    
    n=int(input('spune_un nr='))
    incercari+=1
    if(n==m):
        print('corect')
        
    elif (n>m):
        print('nr e prea mare')
        
    else:
        print('nr e prea mic')
print('incerceri',incercari)