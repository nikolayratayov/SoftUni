bit = int(input())
kit = float(input())
kom = float(input())
bit_e = bit*1168/1.95
kit_e = kit*0.15*1.76/1.95
kom_e = kom/100*(bit_e+kit_e)
result = bit_e+kit_e-kom_e
print('%.2f' % result)
