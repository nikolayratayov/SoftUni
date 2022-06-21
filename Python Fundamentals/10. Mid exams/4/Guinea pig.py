food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
fail = False
for i in range(1, 31):
    food -= 300
    if i % 2 == 0:
        hay -= food * 0.05
    if i % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        fail = True
        break
food = food / 1000
hay = hay / 1000
cover = cover / 1000
if fail:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')
