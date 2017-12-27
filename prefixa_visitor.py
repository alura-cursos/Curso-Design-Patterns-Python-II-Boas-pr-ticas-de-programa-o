class Prefixa_Visitor(object):

    def visita_soma(self, soma):

        print '+',
        print '(',
        soma.expressao_esquerda.aceita(self)
        soma.expressao_direita.aceita(self)
        print ')',

    def visita_subtracao(self, subtracao):
        print '-',
        print '(',
        subtracao.expressao_esquerda.aceita(self)
        subtracao.expressao_direita.aceita(self)
        print ')',

    def visita_numero(self, numero):

        print numero.avalia(),