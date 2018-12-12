from Node import Node
from Problema import Problema
import csv
import time
import sys

class Agente(object):

    explorados = []
    fronteira = []
    mapa = []

    def __init__(self,*args):
        
        attr = str(args[0]).replace('[','').replace(']','').replace(' ','').replace("'",'').split(',')       
        if len(attr) < 5:
            self.opencsv(attr[3])
            node1 = Node(attr[1],Problema(attr[2]),None,0)
            self.fronteira.append(node1)
            self.busca() 
        else:
            self.opencsv(attr[4])
            node1 = Node(attr[1],Problema(attr[2]),None,0)
            node2 = Node(attr[2],Problema(attr[3]),None,0)
            self.fronteira.append(node1)
            self.busca()
            self.explorados = []
            self.fronteira = []
            self.fronteira.append(node2)
            self.busca()     

    def opencsv(self,mapaCsv):
        with open(mapaCsv, 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                self.mapa.append([row['current'],row['goal'],int(row['distance'])])

    def busca(self):

        if (len(self.fronteira) is 0):
            return False

        parent = self.fronteira.pop(0)

        if parent.problema.verificaEstado(parent.estadoAtual):
            self.exibeCaminho(parent)
            return True    

        self.explorados.append(parent)

        for possibilidade in parent.problema.possibilidades(parent.estadoAtual,self.mapa):
            child = Node(possibilidade[1],parent.problema,parent,parent.custo + int(possibilidade[2]))
            if child not in self.fronteira and child not in self.explorados:
                self.fronteira.append(child)
            else:
                for f in self.fronteira:
                    if child.estadoAtual == f.estadoAtual and child.custo < f.custo:
                        f = child
        self.fronteira.sort(key=lambda x: x.custo)
        self.busca()

    def exibeCaminho(self, result):
        temp = result
        tempVet = []
        i = 1
        while temp is not None:
            tempVet.append(temp)
            temp = temp.node
        for item in reversed(tempVet):
            print('passo'+str(i)+' em ' + str(item.estadoAtual) + ' com distancia ' + str(item.custo))
            i = i + 1


inicio = time.time()
Agente(sys.argv)
fim = time.time()
print('run time ' + str(fim - inicio) + " seconds")