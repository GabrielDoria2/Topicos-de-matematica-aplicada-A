'''
UFRJ - Universidade Federal do Rio de Janeiro
IM -Instituto de Matemática
DMA - Departamento de Matemática Aplicada
Aluno: Gabriel Pedrosa Dória
 DRE 119065076
'''

x = int(input("Digite um número para que seus dígitos sejam somados: "))

soma = 0
while x > 0:
    resto = x % 10
    x = x // 10
    soma = soma + resto

print("O valor é", soma)
