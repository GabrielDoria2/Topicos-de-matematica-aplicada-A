// UFRJ - Universidade Federal do Rio de Janeiro
// IM -Instituto de Matemática
// DMA - Departamento de Matemática Aplicada
// Aluno: Gabriel Pedrosa Dória
// DRE 119065076
#include<stdio.h>
#include<math.h>

int main() {

    double a, b, c, delta, x1, x2;
    scanf ("%lf%lf%lf", &a,&b,&c);
    delta = b*b-4*a*c;
    x1 = (-b+sqrt(delta))/(2*a);
    x2 = (-b-sqrt(delta))/(2*a);
    if(delta<0 || a == 0){
        printf ("Impossivel calcular\n");
    }
    else{
        printf ("R1 = %.5lf\nR2 = %.5lf\n", x1, x2);
    }
    return 0;
}

