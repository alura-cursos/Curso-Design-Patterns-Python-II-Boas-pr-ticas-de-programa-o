# -*- coding: utf-8 -*-

from datetime import date

class Pedido(object):

    def __init__(self, cliente, valor):

        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

class Fila_de_trabalho(object):

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


from abc import ABCMeta, abstractmethod
class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

class Conclui_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()

class Paga_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()

if __name__ == '__main__':

    pedido1 = Pedido('Flávio', 150)
    pedido2 = Pedido('Almeida', 250)

    fila_de_trabalho = Fila_de_trabalho()
    fila_de_trabalho.adiciona(Paga_pedido(pedido1))
    fila_de_trabalho.adiciona(Paga_pedido(pedido2))
    fila_de_trabalho.adiciona(Conclui_pedido(pedido1))

    fila_de_trabalho.processa()