import datetime
date1 = input()
date2 = datetime.datetime.strptime(date1, '%d-%m-%Y')
date3 = date2 + datetime.timedelta(days=1000)
print(date3.strftime('%d-%m-%Y'))