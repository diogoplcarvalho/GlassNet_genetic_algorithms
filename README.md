# Algoritmos Genéticos: Trabalho final

## Equipe: Diogo P. de L. Carvalho, José D. A. Sales e Mayllon E. P. S. Silva

### Introdução
<p align="justify">Este repositório contém o projeto final do curso de Algoritmos Genéticos, que visa otimizar a formulação de vidros à prova de bala. Utilizando dados de uma base de dados contendo diversos compostos de formação de vidros, nosso objetivo é melhorar significativamente as propriedades de resistência balística do vidro enquanto mantemos os menores custos possíveis de produção. Este projeto combina a ciência dos materiais com técnicas avançadas de otimização baseada em algoritmos genéticos para encontrar soluções inovadoras e economicamente viáveis. Os dados dos compostos a serem trabalhados estão disponíveis no “Glasspy” [1], esse módulo por sua vez, não oferece as informações necessárias para trabalharmos com os preços dos compostos, para solucionar esse problema, utilizamos os preços do “Sigma Aldrich”[2], uma empresa referência no fornecimento de produtos para pesquisa científica</p>

### Contexto
<p align="justify">Vidros à prova de bala são materiais críticos em uma variedade de aplicações que vão desde a proteção de veículos até a segurança de instalações. A eficácia desses vidros depende de sua capacidade de absorver e dissipar a energia de impactos de alta velocidade, impedindo a penetração de projéteis. A resistência balística do vidro é fortemente influenciada pela sua composição química. Diferentes compostos e aditivos podem conferir ao vidro propriedades como maior dureza, resistência ao impacto, e tenacidade. Contudo, a introdução desses compostos pode aumentar substancialmente os custos de produção, tornando imperativo encontrar um equilíbrio entre desempenho e custo. O desenvolvimento de vidros à prova de bala envolve um complexo processo de experimentação e ajuste fino das formulações químicas. Tradicionalmente, esse processo pode ser caro e demorado. Aqui, entra a aplicação de algoritmos genéticos, que oferecem uma abordagem eficiente para explorar um vasto espaço de combinações de compostos e identificar aquelas que maximizam a resistência balística a um custo reduzido.</p>

### Objetivo
<p align="justify">O objetivo deste projeto é determinar vidros de custo acessíveis que apresentem alta resistência balística, em específico, objetivamos maximizar o módulo de Young e a microdureza do material, enquanto buscamos as melhores alternativas para minimizar, utilizando algoritmos genéticos, o custo das matérias-primas na produção desses vidro. </p>

### Sobre o Dataset e o Modelo Preditivo

<p align="justify">A base de dados utilizada nesse trabalho é o “SciGlass”[3], o SciGlass é um banco de dados abrangente de propriedades de vidros, projetado para auxiliar na pesquisa e desenvolvimento de novos tipos de vidros. A database SciGlass 7.7 possui dados de mais de 300 mil composições, incluindo óxidos, halogenetos e calcogenetos. Para acessarmos essa grande base de dados, utilizamos o módulo GlassPy [1] como intermediador. Glasspy é um módulo em python também voltado a pesquisas relacionadas a materiais vítreos. O glasspy oferece um método conveniente para carregar dados do SciGlass em um dataframe do tipo Pandas. O GlassPy também abarca o GlassNet [4], que é um modelo preditivo para várias propriedades de vidros.</p>

<p align="justify">O GlassNet é uma rede neural multitask profunda treinada com mais 218 mil exemplos de diferentes composições vítreas. O modelo tem a capacidade de prever 85 diferentes propriedades, sejam elas óticas, elétricas, dielétricas, mecânicas e térmicas em diferentes tipos de composições. O modelo foi treinado com os dados do SciGlass e está disponível no módulo Glasspy como código aberto a comunidade científica. </p>

### Estratégias para o trabalaho
<ul>
  <li>Preparação dos Dados</li>
  <p align="justify">Utilizando o Glasspy como intermediador, os dados do SciGlass foram importados e transformados em um DataFrame do tipo Pandas, essa conversão foi precisa para uma visualização mais agradável dos dados. Análises estatísticas foram feitas com os diferentes tipos de colunas presentes no dataset, sendo elas</p>
  <ul>
    <li>Elements (Elementos)</li>
    <li>Compoundns (Compostos)</li>
    <li>Property (Propriedades)</li>
    <li>Metadata (Metadados)</li>
  </ul> <br>
  <p align="justify">Dentre as colunas acima, a de interesse em nosso trabalho é apenas a coluna de Compostos e Propriedades. Dentre o total de propriedades oferecidas pelo GlassPy foram escolhidas duas para serem melhoradas no algoritmo genético, essas duas propriedades foram escolhidas com base na sua importância e contribuição para a formação de um vidro a prova de balas eficiente. Em conjunto e com orientação do professor orientador foram escolhidas as seguintes propriedades</p>
  <ul>
    <li>Young's Modulus (Módulo de Young)</li>
    <p align="justify">O módulo de Young, também conhecido como módulo de elasticidade, é uma medida da rigidez de um material. Ele quantifica a relação entre a tensão (força por unidade de área) e a deformação (deformação relativa) em um material elástico quando este é submetido a uma carga de tração ou compressão (Capacidade do material resistir a deformação elástica) </p>

  <li>Microhardness (Microdureza)</li>
  <p align="justify">A microdureza é uma medida da dureza de um material em uma escala microscópica. É determinada aplicando uma pequena carga controlada a um indentador muito pequeno e medindo a impressão deixada no material.</p>
  </ul>
<p align="justify"> Em nosso projeto, objetivamos maximizar essas duas propriedades, porém, com a restrição da minimização do preço do composto, restringimos nossa busca a apenas os compostos óxidos e obtivemos um total de 196 composições. Para a busca de preços de cada composto contemplado no GlassPy, fizemos a coleta de preços em dólar (USD) por grama de cada composto de acordo com os valores do Sigma Aldrich. Os valores obtidos foram guardados em um dicionário com o intuito de ser usado posteriormente na execução do algoritmo genético. Importante ressaltar que em nossa busca nem todos os preços foram encontrados. Os valores faltantes então, foram posteriormente removidos do dicionário.</p>
  
  <li>Algoritmo Genético</li>
</ul>


### References:
[1] GlassPy documentation — GlassPy latest documentation. Disponível em: <https://glasspy.readthedocs.io/en/latest/>. Acesso em: 22 maio. 2024. <br>
[2] Sigma-Aldrich: Analytical, Biology, Chemistry & Materials Science products and services. Disponível em: <https://www.sigmaaldrich.com>. <br>
[3] SciGlass. Disponível em: <https://www.akoscheminformatics.de/sciglass/sciglass.htm>. Acesso em: 25 maio. 2024.<br>
[4] CASSAR, D. R. GlassNet: A multitask deep neural network for predicting many glass properties. Ceramics international, v. 49, n. 22, p. 36013–36024, 1 nov. 2023.<br>

‌

‌
