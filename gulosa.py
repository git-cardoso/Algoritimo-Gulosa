# coding: utf-8


class Vertice:

    def __init__(self, nome_cidade, distancia_objetivo):
        self.nome_cidade = nome_cidade
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def mostra_cidade(self):
        for i in self.cidades:
            print(i.vertice.nome_cidade, i.custo)


class Cidade:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo


class Grafo:
    portoUniao = Vertice("Porto União", 203)
    pauloFrontin = Vertice("Paulo Frontin", 172)
    canoinhas = Vertice("Canoinhas", 141)
    irati = Vertice("Irati", 139)
    palmeira = Vertice("Palmeira", 59)
    campoLargo = Vertice("Campo Largo", 27)
    curitiba = Vertice("Curitiba", 0)
    balsaNova = Vertice("Balsa Nova", 41)
    araucaria = Vertice("Araucária", 23)
    saoJose = Vertice("São José dos Pinhais", 13)
    contenda = Vertice("Contenda", 39)
    mafra = Vertice("Mafra", 94)
    tijucas = Vertice("Tijucas do Sul", 56)
    lapa = Vertice("Lapa", 74)
    saoMateus = Vertice("São Mateus do Sul", 123)
    tresBarras = Vertice("Três Barras", 131)
    
    portoUniao.adicionar_cidade(Cidade(pauloFrontin, 46))  
    portoUniao.adicionar_cidade(Cidade(canoinhas, 78))
    portoUniao.adicionar_cidade(Cidade(saoMateus, 87))
    pauloFrontin.adicionar_cidade(Cidade(portoUniao, 46))
    pauloFrontin.adicionar_cidade(Cidade(irati, 75))
    canoinhas.adicionar_cidade(Cidade(portoUniao, 78))
    canoinhas.adicionar_cidade(Cidade(tresBarras, 12))
    canoinhas.adicionar_cidade(Cidade(mafra, 66))
    irati.adicionar_cidade(Cidade(pauloFrontin, 75))
    irati.adicionar_cidade(Cidade(palmeira, 75))
    irati.adicionar_cidade(Cidade(saoMateus, 57))
    palmeira.adicionar_cidade(Cidade(irati, 75))
    palmeira.adicionar_cidade(Cidade(saoMateus, 77))
    palmeira.adicionar_cidade(Cidade(campoLargo, 55))
    campoLargo.adicionar_cidade(Cidade(palmeira, 55))
    campoLargo.adicionar_cidade(Cidade(balsaNova, 22))
    campoLargo.adicionar_cidade(Cidade(curitiba, 29))
    curitiba.adicionar_cidade(Cidade(campoLargo, 29))
    curitiba.adicionar_cidade(Cidade(araucaria, 37))
    curitiba.adicionar_cidade(Cidade(saoJose, 15))
    balsaNova.adicionar_cidade(Cidade(curitiba, 51))
    balsaNova.adicionar_cidade(Cidade(campoLargo, 22))
    balsaNova.adicionar_cidade(Cidade(contenda, 19))
    araucaria.adicionar_cidade(Cidade(curitiba, 37))
    araucaria.adicionar_cidade(Cidade(contenda, 18))
    saoJose.adicionar_cidade(Cidade(curitiba, 15))
    saoJose.adicionar_cidade(Cidade(tijucas, 49)) 
    contenda.adicionar_cidade(Cidade(balsaNova, 19))
    contenda.adicionar_cidade(Cidade(araucaria, 18))
    contenda.adicionar_cidade(Cidade(lapa, 26))
    mafra.adicionar_cidade(Cidade(tijucas, 99))
    mafra.adicionar_cidade(Cidade(lapa, 57))
    mafra.adicionar_cidade(Cidade(canoinhas, 66))
    tijucas.adicionar_cidade(Cidade(mafra, 99))
    tijucas.adicionar_cidade(Cidade(saoJose, 49))
    lapa.adicionar_cidade(Cidade(contenda, 26))
    lapa.adicionar_cidade(Cidade(saoMateus, 60))
    lapa.adicionar_cidade(Cidade(mafra, 57))
    saoMateus.adicionar_cidade(Cidade(palmeira, 77))
    saoMateus.adicionar_cidade(Cidade(irati, 57))
    saoMateus.adicionar_cidade(Cidade(lapa, 60))
    saoMateus.adicionar_cidade(Cidade(tresBarras, 43))
    saoMateus.adicionar_cidade(Cidade(portoUniao, 87))
    tresBarras.adicionar_cidade(Cidade(saoMateus, 43))
    tresBarras.adicionar_cidade(Cidade(canoinhas, 12))

grafo = Grafo()


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = list(range(self.capacidade))

    def insere(self, vertice):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0

        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'[ {i} ]  -  {self.valores[i].nome_cidade}  a {self.valores[i].distancia_objetivo}')

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print(f'Passando pela cidade : {atual.nome_cidade}')
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.cidades))
            for Cidade in atual.cidades:
                if Cidade.vertice.visitado == False:
                    Cidade.vertice.visitado == True
                    vetor_ordenado.insere(Cidade.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0])


busca_gulosa = Gulosa(grafo.curitiba)
busca_gulosa.buscar(grafo.portoUniao)
