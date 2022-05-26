n = int(input())
dict_of_synonyms ={}
for i in range(n):
    a = input()
    b = input()
    if a not in dict_of_synonyms:
        dict_of_synonyms[a] = list()
        dict_of_synonyms[a].append(b)
    else:
        dict_of_synonyms[a].append(b)

for key, value in dict_of_synonyms.items():
    print(f'{key} - {", ".join(value)}')