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
            linha += [int(numeros[2+i*m + j])]
            mat += [linha]

    print(mat)

def printmatriz():
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()

lendomatriz()
printmatriz()
