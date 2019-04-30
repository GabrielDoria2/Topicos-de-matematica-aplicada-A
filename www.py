mat = []
m = n = 0
def lendomatriz():
    global m, n, mat
    arq = open('bb.txt')
    conteudo= arq.read()

    numeros = conteudo.split()

    m = int(numeros[0])
    n = int(numeros[1])

    print ("A matriz tem {} linhas e {} colunaas".format(m,n))


    for i in range(m):
        linha = []
        for j in range(n):
            try:
                linha += [float(numeros[2+i*m + j])]
            except ValueError as err:
             print(err)
             linha += ["NaN"]
        mat += [linha]

    print(mat)

def printmatriz():
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

def printmatrizalinhada():
    print("+","-"*17,"+","-"*17,"+","-"*17,"+")
    for i in range(m):
        print("|",end=" ")
        for j in range(n):
            print(" {0:^15f} ".format ( mat[i][j]), end = " | ")
        print() #pula para próxima linha
        print("+","-"*17,"+","-"*17,"+","-"*17,"+")


lendomatriz()
printmatriz()
printmatrizalinhada()
