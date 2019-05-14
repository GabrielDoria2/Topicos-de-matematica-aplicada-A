#-----------------------------------------------------------------------------
# UFRJ - Universidade Federal do Rio de Janeiro
#   IM - Instituto de Matematica
#  DMA - Departamento de Matematica Aplicada
#
# TMAA - MAE 353 - Programacao I
#
#Gabriel Pedrosa Dória
#DRE: 119065076
#
#Diego Rodrigues Nascimento
#119106458
#
# 12 de maio de 2019
#----------------------------------------------------------------------------
 
def criamatriz(i,j, valor):
	matriz = []
	for i in range (i):
		#cria linha i
		linha = []
		for j in range (j):
			linha.append(valor)
			#adiciona linha à matriz

		matriz.append(linha)
return matriz

# Rotina que imprime uma matriz no formato linhas e colunas de floats
def PrintMatriz():
  for i in range(m):
    for j in range(n):
      print(mat[i][j], end=" ")
    print() # pula para proxima linha de texto

    def somar(m1, m2):
    	matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma


def mult_escalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

 def addMatrix(lin, colun, matriz):
    lin = linhas
    colun = colunas

    for i in range(linhas,):
        soma.append([])
        for j in range(colunas):
            x = linhas[i][j]+colunas[i][j]
            somarMatriz[i].append(x)


def prodMatrix(A,B):
 """Multiplica duas matrizes."""
 sizeL=len(A)
 sizeC=len(A[0])
 C=nullMatrix(sizeL,sizeC)
 # Multiplica
 for i in range(sizeL):
  for j in range(sizeC):
   val=0
   for k in range(len(B[0])):
    val = val + A[i][k]*B[k][j]
   C[i][j]=val
 return C

def transposeMatrix(M):
 """Calcula a transposta de uma matriz."""
 aux=[]
 for j in range(len(M[0])):
  linha=[]
  for i in range(len(M)):
   linha.append(M[i][j])
  aux.append(linha)
 return aux

 def permutacao(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])
	cont = 0
	cont2 = 0
	
	for i in range(linhas):
		for j in range (colunas):
			if matriz[i][j] != 0:
				cont+=1
				col = j
				#
		
			if matriz[j][i] != 0:
				cont2+=1
		if cont > 1 or cont2>1:
			return False
		cont = 0
		cont2= 0
	return True	

	def Apresenta_menu_opcoes():
    print("\n+---------------------------------+")    
    print("\t1 - Multiplicação escalar")
    print("\t2 - Soma de matrizes"    )
    print("\t3 - Produto de matrizes")
    print("\t4 - Matriz transposta")
    print("\t5 - Permutação")
    print("+---------------------------------+\n"    )

def Executa():
    fim = False
    while not fim :

        Apresenta_menu_opcoes()
        opcao = input("Entre a sua opcao: ")
        if   opcao == '1': print("mult_escalar()")
        elif opcao == '2': print("addMatrix()")
        elif opcao == '3': print("prodMatrix()")
        elif opcao == '4': print("transposeMatrix()")
    elif opcao == '5': print("permutacao()")
        else: 
            if opcao != '6': print("Comando nao valido")
            else: fim = True

criamatriz()
PrintMatriz()
Executa() 
