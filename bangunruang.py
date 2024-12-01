import math

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'luas balok adalah {hitung}')

def l_kubus(l, s): 
    hitung = 6 * (s* s)   
    print(f'luas kubus adalah {hitung}') 

def l_limas(l, a, t): 
    hitung = (1/2*a*t) + (3 * l) 
    print(f'luas limas adalah {hitung}') 

def l_tabung(l, r, t):
    hitung = 2 * (r * t)
    print(f'luas tabung adalah {hitung}') 

def L_prisma(l, k, t):
    hitung = 2 * l + k * t
    print(f'hitung luas prisma adalah {hitung}')       