n = int(input())
if n != 0:
	count = 1
else:
	count = 0
a = 9999999999
hmm = 0
for i in range(1, n + 1):
	b = a
	a = int(input())
	if a > b:
		count += 1
	else:
		if count > hmm:
			hmm = count
		count = 1
if hmm >= count:
	print(hmm)
else:
	print(count)
