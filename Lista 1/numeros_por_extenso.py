# Tópicos de matemática aplicada A
# Rio de Janeiro, 25 de março de 2019
# Gabriel Pedrosa Dória
# DRE: 119065076

class dExtenso():
    trioextenso=()
    classextenso=()

    def __init__(self):
        self.trioextenso=(
                     ("dummy","um","dois","três","quatro","cinco","seis","sete",
                     "oito","nove"),
                     ("dez","onze","doze","treze","quatorze","quinze","dezesseis",
                     "dezessete","dezoito","dezenove"),
                     ("dummy","dummy","vinte","trinta","quarenta","cinquenta",
                     "sessenta","setenta","oitenta","noventa"),
                     ("dummy","cento","duzentos","trezentos","quatrocentos",
                     "quinhentos","seiscentos","setecentos","oitocentos",
                     "novecentos"))
        self.classextenso=(
                      "dummy","mil","milh","bilh","trilh","quatrilh",
                      "quintilh","sextilh","septilh","octilh",
                      "nonilh","decilh","undecilh","duodecilh",
                      "tredecilh","quatordecilh","quindecilh",
                      "sexdecilh","setedecilh","octodecilh",
                      "novedecilh","vigesilh" )

    def escrever_trio_extenso(self, trio):

        saida=[]

        if trio == '100':
            return 'cem'
        elif trio == '000':
            return 'zero'
        else:
            c, d, u = trio
            c, d, u = int(c), int(d), int(u)

            if c != 0:
                saida.append(self.trioextenso[3][c])
            if d == 1:
                saida.append(self.trioextenso[1][u])
            else:
                if d != 0:
                    saida.append(self.trioextenso[2][d])
                if u != 0:
                    saida.append(self.trioextenso[0][u])
        return ' e '.join(saida)

    def nao_e_ultimo_trio(self, totalTrios, contador):
        return contador < (totalTrios - 1)

    def trio_a_esquerda_eq_zero(self, trioLista, contador):
        t = len(trioLista)-1
        return trioLista[t-contador-1] == '000'

    def getExtenso(self, num, quebradelinhas=0):
        num = num.lstrip('0')
        pad = 3 - len(num)%3
        if pad < 3: num = '0'*pad + num

        it = iter(num)
        trioLista = [ ''.join([a,b,c]) for a, b, c in zip(it, it, it)]

        if len(trioLista) > len(self.classextenso):
            print ('Número muito grande')

        contador=0
        saida=''
        extensofinal=''

        for trio in reversed(trioLista):
            trioInt=int(trio)

            if trioInt > 0:
                saida = self.escrever_trio_extenso(trio)
                if contador > 0:
                    saida = saida + ' ' + self.classextenso[contador]
                if contador > 1:
                    if trioInt > 1:
                        saida = saida + 'ões'
                    else:
                        saida = saida + 'ão'
                if quebradelinhas == 0:
                    if self.nao_e_ultimo_trio(len(trioLista), contador):
                        if self.trio_a_esquerda_eq_zero(trioLista, contador):
                            saida = ' e ' + saida
                        elif trioInt >= 100:
                            saida = ', ' + saida
                        else:
                            saida = ' e ' + saida
                else:
                    saida = saida + '\n'

                extensofinal = saida + extensofinal
            contador = contador + 1
        return extensofinal.rstrip('\n')

if __name__ == '__main__':
    import sys
    argc = len(sys.argv)

    if argc < 2:
        print ('[uso] %s <numero>' % (sys.argv[0]))
    else:
        n = dExtenso()
        print (n.getExtenso(sys.argv[1], quebradelinhas=0))
