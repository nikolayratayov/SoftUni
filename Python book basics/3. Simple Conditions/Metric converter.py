chislo = float(input())
vhod = input().lower()
izhod = input().lower()
if vhod == 'mm':
    chislo = chislo/1000
elif vhod == 'cm':
    chislo = chislo/100
elif vhod == 'mi':
    chislo = chislo/0.000621371192
elif vhod == 'in':
    chislo = chislo/39.3700787
elif vhod == 'km':
    chislo = chislo/0.001
elif vhod == 'ft':
    chislo = chislo/3.2808399
elif vhod == 'yd':
    chislo = chislo/1.0936133
if izhod == 'mm':
    chislo = chislo*1000
elif izhod == 'cm':
    chislo = chislo*100
elif izhod == 'mi':
    chislo = chislo*0.000621371192
elif izhod == 'in':
    chislo = chislo*39.3700787
elif izhod == 'km':
    chislo = chislo*0.001
elif izhod == 'ft':
    chislo = chislo*3.2808399
elif izhod == 'yd':
    chislo = chislo*1.0936133
print(f'{chislo} {izhod}')
