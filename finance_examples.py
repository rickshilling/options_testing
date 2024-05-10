import finance as f
from functools import partial

def A(t):
    match t:
        case 0:
            answer = 100
        case 1:
            answer = 110
    return answer

print(f.K_A(A))

def S(t,p):
    match t:
        case 0:
            answer = 50
        case 1:
            answer = p*52 + (1-p)*48
    return answer

S_1 = partial(S,t=1)
print(S_1(p=0.3))

pass