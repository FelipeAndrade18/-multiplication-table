print('{:=^40}'.format('\033[1;30mTABUADA\033[m'))
n1 = int(input('Digite um numere para saber sua TABUADA:'))
mult = 0
for t in range(1, 11):
        mult = n1 * t
        print('{} x {:2} = {}'.format(n1, t, mult))