'''
UFRJ - Universidade Federal do Rio de Janeiro
IM -Instituto de Matemática
DMA - Departamento de Matemática Aplicada
Aluno: Gabriel Pedrosa Dória
 DRE 119065076
'''
def fibonacci(n):
    if(n==1):
        return 0
    elif (n==2):
        return 1
    else:
       fib2=0
       fib1=1
       for i in range(3,n+1):
           fib=fib2+fib1
           fib2=fib1
           fib1=fib
       return fib

if __name__ == '__main__':
    theSum=0
    count=1
    fib=fibonacci(count)
    while(fib<4000000):
        if(fib%2==1):
            theSum=theSum+fib
        count=count+1
        fib=fibonacci(count)

    print (theSum)       
