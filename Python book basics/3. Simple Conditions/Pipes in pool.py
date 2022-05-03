v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
v_new = (p1+p2)*h
if v_new <= v:
    a = (v_new*100)//v
    p1_a = p1*h
    p1_percent = (p1_a*100)//v_new
    p2_a = p2*h
    p2_percent = (p2_a*100)//v_new
    print(f'The pool is {a}% full. Pipe 1: {p1_percent}%. Pipe 2: {p2_percent}%.')
else:
    prel = v_new-v
    print(f'For {h} hours the pool overflows with {prel} liters.')
