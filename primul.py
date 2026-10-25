
import random
print('!!!WELCOME!!!')
max_incercari=7
d='da'
while d == 'da':
    m = random.randint(1, 20)
    n = 0
    incercari = 0

    while n != m and incercari < max_incercari:
        n = int(input('spune_un nr='))
        incercari += 1

        if n == m:
            print('corect')
        elif n > m:
            print('nr e prea mare')
        else:
            print('nr e prea mic')

        if incercari == max_incercari and n != m:
            print('ai pierdut')

        print('incercari=', incercari)

    d = input('try again? (da/nu): ').strip().lower()

print('thank you for playing!') 