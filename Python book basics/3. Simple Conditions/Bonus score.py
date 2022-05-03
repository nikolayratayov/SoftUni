number = int(input())
if number <= 100:
    number_n = number + 5
elif 100 < number <= 1000:
    number_n = number*0.2+number
elif number > 1000:
    number_n = number*0.1+number
if number % 2 == 0:
    number_new = number_n+1
elif number % 10 == 5:
    number_new = number_n+2
else:
    number_new = number_n
print(number_new-number)
print(number_new)
