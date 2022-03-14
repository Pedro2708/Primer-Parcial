#Algoritmo para encontrar la solución mas optima al problema de las 8 reinas
#Donde el jugador ingresa la cantidad de reinas para ejecutar el algoritmo
#Pedro Jose Hernandez Guzman 1490-18-16038


def free(row, col, n):
    
    
    for i in range(n):
        if tablero[row][i] == 'R' or tablero[i][col] == 'R':
            return False

    if row <= col:
        c = col - row
        r = 0
    else:
        r = row - col
        c = 0
    while c < n and r < n:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c += 1

    if row <= col:
        r = 0
        c = col + row
        if c > n-1:
            r = c - (n-1)
            c = n-1
    else:
        c = n-1
        r = row - ((n-1) - col)

    while c >= 0 and r < n:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c -= 1

    return True

def agregar_reina(n,m):
   
    if m < 1:
        return True

    for idx_row in range(n):
        for idx_col in range(n):
            if free(idx_row, idx_col, n):
                tablero[idx_row][idx_col] = 'R'
                if agregar_reina(n,m-1):
                    return True
                else:
                    tablero[idx_row][idx_col] = '*'

    return False

n= int(input("Ingrese la cantidad de reinas para la IA: "))
m=n
tablero = []
for i in range(n):
    tablero.append(['*'] * n)
agregar_reina(n,m)
for row in tablero:
    print(*row)
