import di_graphs as dg
import graph as gp


def abrir_arquivo(arquivo):
    try:
        arq = open(arquivo, "r")
        arq.seek(0)
        file = arq.readlines()
        # print(file)
    finally:
        arq.close()

    return file

grafo
sel = int(input())
print("Digite 1 se o seu grafo é direcionado")
print("Digite 2 se o seu grafo é não direcionado")

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
            grafo = gp.Grafo(graph, vertices)  # Lista e tupla
        elif select == 2:
            Vertices = input("Digite seus vertices: ").split(",")
            Arestas = input("Digite suas arestas: ").split(",")

    print("Digite 1 para Imprimir o grafo")
    print("Digite 2 para Imprimir a ordem do grafo")
    print("Digite 3 para Imprimir o tamanho do grafo")
    print("Digite 4 para Imprimir os verteces adjacentes")
    print("Digite 5 para Imprimir o grau do grafo")
    print("Digite 6 para verificar se dois vertices são adjacentes")
    print("Digite 7 para Imprimir o menor caminho e custo do  grafo")
    print("Digite 8 para Imprimir o vertice de maior grau")

    sele = int(input("Digite a sua escolha: "))
    if sele == 1:
        dg.criaDiGraph(grafo)

elif sel == 2:
    print("Digite 1 para Imprimir o grafo passado")
    print("Digite 2 para Imprimir a ordem do grafo")
    print("Digite 3 para Imprimir o tamanho do grafo")
    print("Digite 4 para Imprimir os verteces adjacentes")
    print("Digite 5 para Imprimir o grau do grafo")
    print("Digite 6 para verificar se dois vertices são adjacentes")
    print("Digite 7 para Imprimir o menor caminho e custo do  grafo")
    print("Digite 8 para Imprimir o vertice de maior grau")

    sele = int(input("Digite a sua escolha: "))
    Vertices = input("Digite seus vertices: ").split(",")
    Arestas = input("Digite suas arestas: ").split(",")

    mgrafo = Vertices.append(Arestas)

    if sele == 1:
        gp.PlotGrafo(mgrafo)
    elif sele ==2:
        gp.n(mgrafo)
    elif sele == 3:
        gp.m(mgrafo)
    elif sele == 4:
        vertice = input("Digite o vertice escolhido: ")
        gp.adjascencia(Vertices, vertice)
    elif sele == 5:
        vertice = input("Digite o vertice escolhido: ")
        gp.GrauDoVertice(mgrafo, vertice)
    elif sele == 6:
        vertice = input("Digite o vertice escolhido: ")
        if vertice in gp.adjascencia(mgrafo):
            print("São adjascentes")
        else:
            print("Não são adjscentes")
    elif sele == 7:
        #menor caminho
    elif sele == 8:
        vertice = input("Digite o vertice escolhido: ")
        gp.GrauDoVerticePorAdjascencia(mgrafo, vertice)


