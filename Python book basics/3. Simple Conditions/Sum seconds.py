a = int(input())
b = int(input())
c = int(input())
summ = a+b+c
minuti = summ // 60
sekundi = summ % 60
if sekundi < 10:
    print(f'{minuti}:0{sekundi}')
else:
    print(f'{minuti}:{sekundi}')
