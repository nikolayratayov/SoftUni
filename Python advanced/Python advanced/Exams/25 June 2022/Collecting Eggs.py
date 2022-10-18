eggs = [int(x) for x in input().split(', ')]
papers = [int(x) for x in input().split(', ')]

boxes = 0

while True:
    if len(eggs) == 0:
        break
    if len(papers) == 0:
        break
    egg = eggs[0]
    paper = papers[-1]
    if egg == 13:
        eggs.pop(0)
        first = papers[0]
        last = papers[-1]
        papers.pop(0)
        papers.pop()
        papers.insert(0, last)
        papers.append(first)
        continue
    if egg <= 0:
        eggs.pop(0)
        continue
    if egg + paper <= 50:
        boxes += 1
    eggs.pop(0)
    papers.pop()

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print('Sorry! You couldn\'t fill any boxes!')
if len(eggs) > 0:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
if len(papers) > 0:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')
