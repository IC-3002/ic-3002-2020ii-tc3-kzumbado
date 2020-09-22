def sumatoria_cubica(n):
    result= 0
    for i in range(0, n+1):
        for j in range (0, i):
            for k in range (j, j+i):
                result = result +1
    return result
    

def sumatoria_constante(n):
    nom = 2*pow(n, 3) + 3*pow(n, 2) + n
    result= nom/6
    return int(result)

