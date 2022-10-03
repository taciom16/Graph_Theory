from cgi import print_form
from re import I
from queue import Queue

# from macpath import split

def abrir_arquivo(arquivo):
        try:
            arq = open(arquivo, "r")
            arq.seek(0)
            file = arq.readlines()
            # print(file)
        finally:
            arq.close()

        return file

class Grafo:
    def __init__(self, Vertices, Arestas):
        self.Vertices = set(Vertices)
        self.Arestas = set(frozenset((u, v)) for u,v in Arestas)

        self.Adjascente = {} #Adjascente -> Item 8

        for i in self.Vertices:
            self.NovoVertice(i)

        for i, j in self.Arestas:
            self.Adjascente[j].add(i)
            self.Adjascente[i].add(j)   

    def adjascencia(self, vertice): #Adjascência de um vértice
        return iter(self.Adjascente[vertice])
        #Printar como list(grafo.adjascencia(3) -> Retorno dessa função é um iterator

    def NovoVertice(self, vertice): #Um vértice por vez -> Item 1
        if vertice not in self.Adjascente:
            self.Vertices.add(vertice)
            self.Adjascente[vertice] = set()

    def NovaAresta(self, j, i): #Uma aresta por vez -> set(grafo.Arestas)
        if j not in self.Adjascente:
            self.NovoVertice(j)

        self.Arestas.add(frozenset([j, i]))
        self.Adjascente[j].add(i)
        self.Adjascente[i].add(j)


    def GrauDoVertice(self, vertice):
        grau = 0    #Implementação do Grau por força bruta, como os exercícios em classe.

        for i in self.Arestas:
            if vertice in i:
                grau += 1

        return grau

    def GrauDoVerticePorAdjascencia(self, vertice):
        return len(self.Adjascente[vertice]) #Diminui a complexidade temporal

    def m(self): #Quantidade de Arestas -> grafo.m()
        return len(self.Arestas)

    def n(self): #Quantidade de Vértices -> grafo.n()
        return len(self.Adjascente)

    def PlotGrafo(self):
        aresta_cpy = []
        for item in self.Arestas:
            aresta_cpy.append(tuple(item))
    
        print(aresta_cpy)

    def ChecarAdjascencia(self, vertice, vertex):

        if vertex in self.Adjascente[vertice]:
            print("Vértices adjascentes")
        else:
            print("Vértices não adjascentes")
    
    def RemoverAresta(self, j, i): #remove uma Aresta
        MinhaAresta = frozenset([j, i])
        if MinhaAresta in self.Arestas:
            self.Arestas.remove(MinhaAresta)
            self.Adjascente[j].remove(i)
            self.Adjascente[i].remove(j)

    def RemoverVertice(self, j): #Remove um vértice
        MeuVertice = list(self.Adjascente[j])
        for i in MeuVertice:
            self.RemoverAresta(j, i)
        del self.Adjascente[j]


    def Dijkstra(self, initial, end):

        explored = []
        queue = [[initial]]

        if initial == end:
            print("Mesma vértice")
            return

        while queue:
            ordem = queue.pop(0)
            node = ordem[-1]

            if node not in explored:
                vizinhos = self.Adjascente[node]

                for vizinho in vizinhos:
                    new_ordem = list(ordem)
                    new_ordem.append(vizinho)
                    queue.append(new_ordem)

                    if vizinho == end:
                        print("O menor caminho é:", *new_ordem)
                        print("O tamanho é:", len(new_ordem))
                        return
                explored.append(node)

        print("Não há conexão entre os vèrtices")
        return

    


print("Digite 1 se o seu grafo é direcionado")
print("Digite 2 se o seu grafo é não direcionado")
sel = int(input("Digite a sua escolha: "))


if sel == 1:
    print("Para inserir por arquivo digite 1")
    print("Para inserir manual digite 2")

    select = input("Digite a sua escolha: ")

    if select == 1:
        if __name__ == '__main__':
            arq = abrir_arquivo("grafo.txt")
            for item in arq:
                if '\n' not in item:
                    vertices = item
                elif '\n' in item:
                    graph = item

            graph = graph.split(",")
            graph1 = graph[-1].split("\n")

            graph1.pop()
            graph.pop()
            graph1 = graph1[0]
            graph.append(graph1)
            grafo = Grafo(graph, vertices)  # Lista e tupla

    elif select == 2:
        Vertices = input("Digite seus vertices: ").split(",")
        Arestas = input("Digite suas arestas: ").split(",")

    # print("Digite 1 para Imprimir o grafo")
    # print("Digite 2 para Imprimir a ordem do grafo")
    # print("Digite 3 para Imprimir o tamanho do grafo")
    # print("Digite 4 para Imprimir os verteces adjacentes")
    # print("Digite 5 para Imprimir o grau do grafo")
    # print("Digite 6 para verificar se dois vertices são adjacentes")
    # print("Digite 7 para Imprimir o menor caminho e custo do  grafo")
    # print("Digite 8 para Imprimir o vertice de maior grau")

    # sele = int(input("Digite a sua escolha: "))
    # if sele == 1:
    #     dg.criaDiGraph(grafo)

elif sel == 2:
    print("Para inserir por arquivo digite 1")
    print("Para inserir manual digite 2")

    select = int(input("Digite a sua escolha: "))

    if select == 1:
        if __name__ == '__main__':
            arq = abrir_arquivo("grafo.txt")
            for item in arq:
                if '\n' not in item:
                    vertices = item
                elif '\n' in item:
                    graph = item

            graph = graph.split(",")
            graph1 = graph[-1].split("\n")

            graph1.pop()
            graph.pop()
            graph1 = graph1[0]
            graph.append(graph1)
            grafo = Grafo(graph, vertices)  # Lista e tupla

    elif select == 2:
        Vertices = input("Digite seus vertices: ").split(",")
        Arestas = input("Digite suas arestas em tuplas: ").split(",")

        print("Digite 1 para Imprimir o grafo passado")
        print("Digite 2 para Imprimir a ordem do grafo")
        print("Digite 3 para Imprimir o tamanho do grafo")
        print("Digite 4 para Imprimir os verteces adjacentes")
        print("Digite 5 para Imprimir o grau do vertice")
        print("Digite 6 para verificar se dois vertices são adjacentes")
        print("Digite 7 para Imprimir o menor caminho e custo do  grafo")
        print("Digite 8 para Imprimir o vertice de maior grau")

        sele = int(input("Digite a sua escolha: "))

        for i in Vertices:
            Grafo.NovoVertice(int(Vertices[i]))
        for i in Arestas:
            Grafo.NovaAresta(int(Arestas[i]))

        if sele == 1:
            Grafo.PlotGrafo()
        elif sele ==2:
            Grafo.n()
        elif sele == 3:
            Grafo.m()
        elif sele == 4:
            vertice = int(input("Digite o vertice escolhido: "))
            Grafo.adjascencia(vertice)
        elif sele == 5:
            vertice = int(input("Digite o vertice escolhido: "))
            Grafo.GrauDoVertice(vertice)
        elif sele == 6:
            vertice1 = int(input("Digite o vertice escolhido: "))
            vertice2 = int(input("Digite o vertice escolhido: "))

            Grafo.ChecarAdjascencia(vertice1, vertice2)
        elif sele == 7:
            inicio = int(input("Digite o vertice inicial: "))
            final = int(input("Digite o vertice final: "))
            Grafo.Dijkstra(inicio, final)
        elif sele == 8:
            vertice = int(input("Digite o vertice escolhido: "))
            Grafo.GrauDoVerticePorAdjascencia(vertice)

                
    


         
    #grafo = Grafo(graph, vertices) #Lista e tupla

    # grafo = Grafo([1,2,3,4,5,6],{(1,2),(2,3),(2,4),(2,5)})

    #grafo.ChecarAdjascencia(2,5)

    # vertice_cpy = []
    # for ver in grafo.Vertices:
    #     vertice_cpy.append(ver)


    '''for node in vertice_cpy:
        for aresta in aresta_cpy:
            if node in aresta: 
                print(f'{node}:{aresta}')'''
    
    #grafo.PlotGrafo()

    #print(list(grafo.adjascencia(2)))

    #grafo.NovaAresta(4,5)

    # grafo.Dijkstra(2,5)

    #print(f"Arestas: {set(grafo.Arestas)}")
    
    #grafo.RemoverVertice(3)
