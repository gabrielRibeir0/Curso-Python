def faz_jogada(N, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if N == 1:
        return 3 if p6 == "o"else 5
    if N == 2:
        return 1
    if N == 3:
        return 7 if p3 == "x" else 9 
    return 4 if N == 0 else 4
'''
Versão longa
def faz_jogada(N, p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if N == 0:
        return 7
    elif N == 1:
        if p4 == "o":
            return 9
        return 1
    elif N == 2:
        return 5
    else:
        if p9 == "x":
            if p1 == "o":
                return 3
            return 1
        else:
            if p3 == "o":
                return 9
            return 3
'''