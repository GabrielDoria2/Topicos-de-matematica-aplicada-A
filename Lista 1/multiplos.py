n = int (input('insira n: '))
x = int (input('insira x: '))
y = int (input('insira y: '))
c = 0
m = 0

while (m < n):
    if c% x == 0 and c% y == 0:
        print (c)
        m+=1
    c +=1
