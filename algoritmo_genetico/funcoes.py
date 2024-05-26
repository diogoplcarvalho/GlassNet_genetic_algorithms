import random
import numpy as np
from glasspy.predict import GlassNet

model = GlassNet()

###############################################################################
#                               Funções Básicas                               #
###############################################################################


def preco_composicao(candidato, lista_de_precos):
    """Define o preço de um candidato.
    
    Args:
      candidato = uma lista contendo os valores dos compostos utilizados em uma composição de vidro do problema.
      lista_de_precos = uma lista contendo os precos dos compostos do candidato.
    """

    candidato = np.array(candidato)
    candidato_grama = candidato/sum(candidato) 
    preco = sum(candidato_grama * np.array(lista_de_precos))

    return preco


###############################################################################
#                                  Compostos                                  #
###############################################################################

def cria_gene(valor_max):
    """Sorteia um valor para um composto óxido para a composição de vidro.
    
    Args:
      valor_max: inteiro represtando o valor máximo do composto.
    """

    valores_possiveis = range(valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato(n, valor_max):
    """Cria uma lista de compostos de uma composição de vidro com n valores entre zero e valor_max.

    Args:
      n: inteiro que representa o número de compostos.
      valor_max: inteiro represtando o valor máximo de um composto.
    """
    
    candidato = []
    for _ in range(n):
        gene = cria_gene(valor_max)
        candidato.append(gene)
    return candidato


def cria_populacao_compostos(tamanho, n, valor_max):
    """Cria uma população para o problema de possíveis composições de vidro.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de compostos.
      valor_max: inteiro represtando o valor máximo de um composto.
    """

    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato(n, valor_max))
    return populacao


def funcao_objetivo(candidato, lista_de_compostos, lista_de_precos, modelo):
    """Computa a função objetivo no problema.

    Args:
      candidato: uma lista contendo os valores dos compostos de uma composição de vidro do problema.
      lista_de_compostos = uma lista contendo os compostos utilizáveos pelo candidato.
      lista_de_precos = uma lista contendo os precos dos compostos do candidato.
      modelo = um modelo de predição de propriedades de vidro a partir de sua composição.
    """
    
    dict_composicao = dict(zip(lista_de_compostos, candidato))
    predicao = modelo.predict(dict_composicao)

    modulo_young = float(predicao['YoungModulus'].iloc[0])
    microdureza = float(predicao['Microhardness'].iloc[0])
    preco = preco_composicao(candidato, lista_de_precos)

    pontuacao = abs((modulo_young/ 85.7) - 1 + (microdureza/5.8) - 1 + (preco/0.72) - 1)
    # pontuacao = (((modulo_young/ 85.7) - 1) ** 2 + ((microdureza/5.8) - 1) ** 2 + ((preco/0.72) - 1) ** 2) ** (1/2)

    return pontuacao


def funcao_objetivo_pop(populacao, lista_de_compostos, lista_de_precos, modelo):
    """Computa a função objetivo para uma população no problema.

    Args:
      candidato: uma lista contendo os valores dos compostos de uma composição de vidro do problema.
      lista_de_compostos = uma lista contendo os compostos utilizáveos pelo candidato.
      lista_de_precos = uma lista contendo os precos dos compostos do candidato.
      modelo = um modelo de predição de propriedades de vidro a partir de sua composição.
    """

    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo(individuo, lista_de_compostos, lista_de_precos, modelo))
    return fitness


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Realiza seleção da população pela roleta.

    Args:
      populacao: lista contendo os individuos do problema.
      fitness: lista contendo os valores computados da funcao objetivo.
    """

    selecionados = random.choices(populacao, fitness, k=len(populacao))
    return selecionados


def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção por minimização de uma população usando torneio.

    Args:
      populacao: lista contendo os individuos do problema.
      fitness: lista contendo os valores computados da funcao objetivo.
      tamanho_torneio: quantidade de invíduos que batalham entre si.
    """

    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.
    """

    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ponto_simples(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.
    """

    if random.random() < chance_de_cruzamento:
        corte = random.randint(1, len(mae) - 1)
        filho1 = pai[:corte] + mae[corte:]
        filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ponto_simples_e_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento
    """

    chance_de_cruzamento_duplo = (1 - chance_de_cruzamento)/2
    chance_de_cruzamento_simples = (1 - chance_de_cruzamento)/2
    chance_aleatoria = random.random()

    if chance_aleatoria < chance_de_cruzamento_duplo:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    elif chance_aleatoria > chance_de_cruzamento_duplo and chance_aleatoria <= chance_de_cruzamento_simples:
        corte = random.randint(1, len(mae) - 1)
        filho1 = pai[:corte] + mae[corte:]
        filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################

def mutacao_sucessiva(populacao, chance_de_mutacao, chance_mutacao_gene, valor_max):
    """Realiza mutação sucessiva no problema.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene.
    """

    for individuo in populacao:
        if random.random() / 2 < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    valor_gene = individuo[gene]
                    sera_maior = random.randint(0, 1)
                    if sera_maior:
                        possivel_valor_gene = valor_gene + random.randint(0, 10)
                        individuo[gene] = possivel_valor_gene if possivel_valor_gene <= valor_max else valor_max
                    else: 
                        possivel_valor_gene = valor_gene - random.randint(0, 10)
                        individuo[gene] = possivel_valor_gene if possivel_valor_gene >= 0 else 0


def mutacao_simples(populacao, chance_de_mutacao, valor_max):
    """Realiza mutação simples no problema.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.
      valor_max: inteiro represtando o valor máximo de um composto.
    """
    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            sera_maior = random.randint(0, 1)
            if sera_maior:
                possivel_valor_gene = valor_gene + random.randint(0, 10)
                individuo[gene] = possivel_valor_gene if possivel_valor_gene <= valor_max else valor_max
            else: 
                possivel_valor_gene = valor_gene - random.randint(0, 10)
                individuo[gene] = possivel_valor_gene if possivel_valor_gene >= 0 else 0