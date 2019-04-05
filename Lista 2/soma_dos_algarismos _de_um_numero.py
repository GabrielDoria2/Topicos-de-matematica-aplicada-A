# Tópicos de matemática aplicada A
# Rio de Janeiro, 25 de março de 2019
# Gabriel Pedrosa Dória
# DRE: 119065076

x = int(input("Digite um número para que seus dígitos sejam somados: "))

soma = 0
while x > 0:
    resto = x % 10
    x = x // 10
    soma = soma + resto

print("O valor é", soma)
