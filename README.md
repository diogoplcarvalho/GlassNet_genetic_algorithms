# Algoritmos Genéticos: Otimização de vidros à prova de bala

## Equipe: Diogo P. de L. Carvalho, José D. A. Sales e Mayllon E. P. S. Silva

### Introdução
<p align="justify">Este repositório contém o projeto final do curso de Algoritmos Genéticos, que visa otimizar a formulação de vidros óxidos à prova de bala. Utilizando dados de uma base de dados contendo diversos compostos de formação de vidros, nosso objetivo é melhorar significativamente as propriedades de resistência balística do vidro enquanto mantemos os menores custos possíveis de produção. Este projeto combina a ciência dos materiais com técnicas de otimização baseada em algoritmos genéticos para encontrar soluções inovadoras e economicamente viáveis a partir de um modelo preditivo de rede neural de propriedades de vidros. Os dados dos compostos e a rede neural que foram trabalhados estão disponíveis no GlassPy <sup>[1]</sup>. Esse módulo por sua vez, não oferece as informações necessárias para trabalharmos com os preços dos compostos, para solucionar esse problema, utilizamos os preços do Sigma Aldrich <sup>[2]</sup>, uma empresa referência no fornecimento de produtos para pesquisa científica.</p>

### Contexto
<p align="justify">Vidros à prova de bala são materiais críticos em uma variedade de aplicações que vão desde a proteção de veículos até a segurança de instalações. A eficácia desses vidros depende de sua capacidade de absorver e dissipar a energia de impactos de alta velocidade, impedindo a penetração de projéteis. A resistência balística do vidro é fortemente influenciada pela sua composição química. Diferentes compostos e aditivos podem conferir ao vidro propriedades como maior dureza, resistência ao impacto e tenacidade. Contudo, a introdução desses compostos pode aumentar substancialmente os custos de produção, tornando imperativo encontrar um equilíbrio entre desempenho e custo. O desenvolvimento de vidros à prova de bala envolve um complexo processo de experimentação e ajuste fino das formulações químicas. Tradicionalmente, esse processo pode ser caro e demorado. Aqui, entra a aplicação de algoritmos genéticos os quais oferecem uma abordagem eficiente para explorar um vasto espaço de combinações de compostos e identificar aquelas que maximizam a resistência balística a um custo reduzido.</p>

### Objetivo
<p align="justify">O objetivo deste projeto é determinar vidros óxidos de custo acessíveis que apresentem alta resistência balística, em específico, objetivamos, utilizando algoritmos genéticos, maximizar o módulo de Young e a microdureza do material, enquanto buscamos as melhores alternativas para minimizar o custo das matérias-primas na produção desses vidros, isso mantendo um quantidade razoável de diferentes compostos utilizados na composição de vidro. Nesse sentido, verifica-se a principal hipótese do projeto <b>H<sub>1</sub></b>: o uso de algoritmos genéricos baseados no modelo preditivo do GlassNet permite encontrar vidros óxidos com alta resistência balística e com custo de produção relativamente baixo.</p>

### Sobre o Dataset e o Modelo Preditivo

<p align="justify">A base de dados utilizada nesse trabalho é o SciGlass<sup>[3]</sup>, um banco de dados abrangente de propriedades de vidros, projetado para auxiliar na pesquisa e desenvolvimento de novos tipos de vidros. O database SciGlass 7.7 possui dados de mais de 300 mil composições, incluindo óxidos, halogenetos e calcogenetos. Para acessarmos essa grande base de dados, em que utilizamos o módulo GlassPy <sup>[1]</sup> como intermediador. GlassPy é um módulo em python também voltado a pesquisas relacionadas a materiais vítreos. O GlassPy oferece um método conveniente para carregar dados do SciGlass em um dataframe do tipo Pandas. O GlassPy também abarca o GlassNet <sup>[4]</sup>, que é um modelo preditivo para várias propriedades de vidros.</p>

<p align="justify">O GlassNet é uma rede neural multitask profunda treinada com mais de 218 mil exemplos de diferentes composições vítreas do SciGlass. O modelo tem a capacidade de prever 85 diferentes propriedades, sejam elas óticas, elétricas, dielétricas, mecânicas e térmicas em diferentes tipos de composições. O modelo foi treinado com os dados do SciGlass e está disponível no módulo GlassPy como código aberto a comunidade científica.</p>

### Ordem de Leitura dos Jupyter Notebooks
Considerando que o objetivo principal e os dados (parte fundamental do projeto) são apresentados no arquivo de análise exploratória, enquanto conceitos mais aprofundados em Algoritmos genéticos são explanados no arquivo de mesmo nome. Com isso, ao leitor do projeto, recomenda-se seguir a seguinte ordem de leitura de arquivos.
<ul>
  <li>analise_exploratoria.ipynb</li>
  <li>algoritmo_genetico.ipynb</li>
</ul>

### Organização do Repositório
* Pasta "analise_exploratoria"
  <ul>
    <li><b>analise_exploratoria.ipynb</b>: Arquivo jupyter contendo a busca dos dados do SciGlass pelo Módulo GlassPy, análise estatística e histogramas das propriedades escolhidas;</li>
    <li><b>prices.csv</b>: Tabela contendo os preços coletados para cada composto óxidos trabalhados no algoritmo genético.</li>
  </ul> <br>
  
* Pasta "algoritmo_genetico
<ul>
  <ul>
    <li><b>algoritmo_genetico.ipynb</b>: Arquivo jupyter contendo o algoritmo genético usado para a otimização dos dados;</li>
    <li><b>funcoes.py</b>: Script python contendo as funções precisas para execução do algoritmo genético. Funções essas que envolvem a criação dos candidatos, população, gene, função objetivo, funções relacionadas as etapas de cruzamento e mutação.</li>
  </ul> </ul>

### Estratégias para o trabalho
<ul>
  <li><b>Preparação dos Dados</b></li>
  <p align="justify">Utilizando o GlassPy como intermediador, os dados do SciGlass foram importados e transformados em um DataFrame do tipo Pandas, essa conversão foi precisa para uma visualização mais agradável dos dados. Análises estatísticas foram feitas com os diferentes tipos de colunas presentes no dataset, sendo elas:</p>
  <ul>
    <li>Elements (Elementos);</li>
    <li>Compoundns (Compostos);</li>
    <li>Property (Propriedades;)</li>
    <li>Metadata (Metadados).</li>
  </ul> <br>
  <p align="justify">Dentre as colunas acima, a de interesse em nosso trabalho é apenas a coluna de Compostos e Propriedades. Dentre o total de propriedades oferecidas pelo GlassPy foram escolhidas duas para serem melhoradas no algoritmo genético, essas duas propriedades foram escolhidas com base na sua importância e contribuição para a formação de um vidro a prova de balas eficiente. Em conjunto e com orientação do professor orientador foram escolhidas as seguintes propriedades.</p>
  <ul>
    <li>Young's Modulus (Módulo de Young)</li>
    <p align="justify">O módulo de Young, também conhecido como módulo de elasticidade, é uma medida da rigidez de um material. Ele quantifica a relação entre a tensão (força por unidade de área) e a deformação (deformação relativa) em um material elástico quando este é submetido a uma carga de tração ou compressão (Capacidade do material resistir a deformação elástica). </p>

  <li>Microhardness (Microdureza)</li>
  <p align="justify">A microdureza é uma medida da dureza de um material em uma escala microscópica. É determinada aplicando uma pequena carga controlada a um indentador muito pequeno e medindo a impressão deixada no material.</p>
  </ul>
<p align="justify"> Em nosso projeto, objetivamos maximizar essas duas propriedades, porém, com a restrição da minimização do preço do composto, restringimos nossa busca a apenas os compostos óxidos e obtivemos um total de 196 composições. Para a busca de preços de cada composto contemplado no GlassPy, fizemos a coleta de preços em dólar (USD) por grama de cada composto de acordo com os valores do Sigma Aldrich. Os valores obtidos foram guardados em um dicionário com o intuito de serem usados posteriormente na execução do algoritmo genético. Importante ressaltar que em nossa busca nem todos os preços foram encontrados. Os valores faltantes então, foram posteriormente removidos do dicionário.</p>
  
  <li><b>Algoritmo Genético</b></li>
  <p align="justify">Utilizando como base o algoritmo genético desenvolvido em sala de aula [7], alteramos o mesmo para que se adequasse ao nosso objetivo. Nossas alterações consistiram principalmente no arquivo de funções, onde foi implementado uma nova função para a etapa de cruzamento juntando os dois tipos de cruzamento vistos: ponto simples e ponto duplo. Alterações nas funções de mutação simples e mutação sucessiva também foram feitas. O fluxo de seleção, cruzamento, mutação e atualização do hall da fama (comum aos algoritmos genéticos) foi implementado nessa etapa do projeto. Para obter-se o resultado do preço do melhor individuo observado utilizou-se sua porcentagem no composto como um todo multiplicado por seu valor em dólares por grama. Foi criado uma função objetivo para calcular a pontuação do candidato a partir de uma equação nova. Dentre as principais alterações feitas com base no script de funções disponibilizado pelo professor, podem-se destacar a função de ativação, a etapa de cruzamento e a etapa de mutação. </p>
  <ul>
    <li><b>Função objetivo</b></li>
    <p align="justify">A função objetivo determina a pontuação do candidato a partir de uma equação inventada pelos colaboradores do projeto, em que o denominador envolve a raiz quadrado de um termo grande, havendo a soma do quadrado do complementar do módulo de young e do da microdureza do candidato normalizado pelo máximo absoluto somado ao quadrado preço normalizado pelo máximo absoluto. Nisso, o numerador representa a raiz cúbica de 1 somado do número de compostos não utilizados dos possíveis na composição, em que tal termo está ao produto de raiz de 3, que permite a normalização de tal função, havendo resultados que variam de 0 a 1 em circunstâncias normais. Veja a fórmula de forma mais clara:</p>
  </ul>
</ul>

$$
Fitness = \frac{\sqrt{(\frac{ModuloYoung}{ModuloYoung_{max}} - 1)^2 + (\frac{Microdureza}{Microdureza_{max}} - 1)^2 + (\frac{Preco}{Preco_{max}})^2}}{\sqrt{3} \cdot \sqrt[3]{NumeroCompostosNaoUtilizados + 1}}
$$  

<ul>
  <ul>
    <li><b>Função de ativação:</b></li>
    <p align="justify">A função cria um dicionário de composição a partir da lista de candidatos e usa um modelo preditivo para estimar as propriedades do vidro. A pontuação é calculada normalizando e combinando os desvios das propriedades e do custo em relação aos valores de referência, esses valores de referência são: No caso das propriedades com o objetivo de maximização (“Microdureza” e Módulo de Young), o valor máximo encontrado no conjunto de dados e no caso de minimização (Preço do composto) o valor mínimo encontrado, com penalização adicional para composições que utilizam poucos compostos ou apresentam valores de “microdureza” e módulo de Young fora de certos limites arbitrariamente estabelecidos. A menor pontuação indica uma melhor composição segundo os critérios estabelecidos. Logo, o fim último da evolução é a minimização da função objetivo.</p>
    <li><b>Etapa de Cruzamento</b></li>
    <p align="justify">Na etapa de cruzamento, utilizamos uma junção dos dois tipos de cruzamento que vimos ao longo do semestre, o cruzamento de ponto simples e cruzamento de ponto duplo, onde cada um ocorrerá apenas se uma condição for atendida com base numa chance aleatória definida.</p>
    <li><b>Etapa de mutação</b></li>
  </ul>
</ul>

### Bibliotecas e Módulos
Nessa etapa, informamos as bibliotecas e módulos utilizados no desenvolvimento do projeto e seu uso nesse projeto. Essas ferramentas vão desde a etapa da análise estatística e visualização dos dados até a otimização de funções no código fonte.

<ul>
  <li><b>Pandas</b>: Biblioteca utilizada para visualização dos dados brutos obtidos do SciGlass e Análise estatística dos mesmos;</li>
  <li><b>GlassPy</b>: Módulo que serviu como intermediador entre o projeto e a base de dados alvo (SciGlass), além de ofercer acesso ao modelo preditivo do GlassNet;</li>
  <ul>
    <li><b>GlassNet</b>: Modelo preditivo (Rede Neural Multitask) utilzada para prever as propriedades do material com base na composição informada;</li>
    <li><b>SciGlass</b>: Base de dados contendo mais de 300 mil composições de materiais vítreos.</li> 
  </ul>
  <li><b>Matplotlib</b>: Biblioteca utilizada para o plot dos gráficos presentes no projeto (histogramas);</li>
  <li><b>Numpy</b>: Biblioetca especializada em trabalhar com arrays multidimensionais e matrizes;</li>
  <li><b>Seaborn</b>: Biblioteca de visualização de dados construida com base no Matplotlib. Utilizada para estilização dos gráficos do projeto;</li>
  
</ul>

### Conclusão
<p align="justify"> A partir dos algoritmos genéticos elaborados nesse projeto, verificou-se no jupyter notebook "algoritmo_genetico.ipynb" que se encontrou ao menos uma suposta composição de vidro com um preço baixo e boas propriedades de resistência balística, considerando o módulo de Young e microdureza.  

### Perspectivas Futuras
* Deseja-se em um futuro próximo, realizar um estudo mais aprofundado sobre a composição de vidros à prova de bala e implementar o algoritmo para considerar mais propriedades importantes que influenciem nessa composição alvo.
* Implementar na função objetivo a restrição dessa composição formar necessariamente vidro, mais um modelo preditivo.
* Extrapolar o projeto para a melhoria não apenas de vidros à prova de bala, mas também para a melhoria de vidros utilizados em aeronaves, com o objetivo de minimização do peso e preço do composto; como também o uso do algoritmo para outros tipos de vidro.

### References:
[1] GlassPy documentation — GlassPy latest documentation. Disponível em: <https://GlassPy.readthedocs.io/en/latest/>. Acesso em: 22 maio. 2024. <br>

[2] Sigma-Aldrich: Analytical, Biology, Chemistry & Materials Science products and services. Disponível em: <https://www.sigmaaldrich.com>. <br>

[3] SciGlass. Disponível em: <https://www.akoscheminformatics.de/sciglass/sciglass.htm>. Acesso em: 25 maio. 2024.<br>

[4] CASSAR, D. R. GlassNet: A multitask deep neural network for predicting many glass properties. Ceramics international, v. 49, n. 22, p. 36013–36024, 1 nov. 2023.<br>

[5] WIKIPEDIA CONTRIBUTORS. Young’s modulus. Disponível em: <https://en.wikipedia.org/wiki/Young%27s_modulus>. <br>

[6] CASSAR, D. R. drcassar/GlassPy. Disponível em: <https://github.com/drcassar/GlassPy>. Acesso em: 25 maio. 2024. <br>

[7] Cassar, Daniel(2024). ATP-303 GA 2.1 - Algoritmo genético. Retirado dos arquivos de Redes Neurais e Algoritimos Genéticos da Ilum - Escola de Ciência.<br>

[8] Cassar, Daniel(2024). ATP-303 GA 3.1 - Caixas não-binárias. Retirado dos arquivos de Redes Neurais e Algoritimos Genéticos da Ilum - Escola de Ciência. <br>
