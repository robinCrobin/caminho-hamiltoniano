# Caminho Hamiltoniano em Grafos

## Descrição do Projeto

Este projeto implementa um algoritmo para encontrar um **Caminho Hamiltoniano** em um grafo orientado ou não orientado. Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez. O problema é clássico em teoria dos grafos e tem alta complexidade computacional (NP-completo).

O algoritmo utiliza a técnica de **backtracking** para explorar todas as possibilidades de caminhos, retornando o primeiro caminho Hamiltoniano encontrado (se existir).

### Funcionamento do Algoritmo

O algoritmo segue os seguintes passos:
1. Para cada vértice do grafo, tenta iniciar um caminho a partir dele.
2. Utiliza uma função recursiva para construir o caminho, marcando os vértices já visitados.
3. Se conseguir visitar todos os vértices sem repeti-los, retorna o caminho encontrado.
4. Caso contrário, retorna que não existe caminho Hamiltoniano.

### Explicação Linha a Linha do Código

#### Função `find_hamiltonian_path(grafo, n)`

- **Linha 4:** Define a função principal que recebe o grafo e o número de vértices.
- **Linha 5:** Define a função interna `backtrack(caminho, visitados)` para realizar a busca recursiva.
- **Linha 6:** Se o tamanho do caminho for igual ao número de vértices, retorna True (caminho completo).
- **Linha 7:** Pega o último vértice do caminho atual.
- **Linhas 8-15:** Para cada vizinho do último vértice, se ainda não foi visitado, adiciona ao caminho e marca como visitado. Chama recursivamente. Se não encontrar, desfaz a escolha (backtracking).
- **Linha 16:** Se nenhum vizinho leva a um caminho Hamiltoniano, retorna False.
- **Linhas 18-22:** Para cada vértice inicial possível, tenta construir um caminho Hamiltoniano a partir dele. Se encontrar, retorna o caminho.
- **Linha 23:** Se não encontrar nenhum caminho, retorna None.

#### Função `main()`

- **Linha 25:** Lê toda a entrada do usuário e separa em uma lista de strings.
- **Linhas 26-29:** Lê o número de vértices (`n`), arestas (`m`) e se o grafo é direcionado (`d`).
- **Linha 30:** Cria o grafo como um dicionário de listas.
- **Linhas 31-36:** Lê as arestas e monta o grafo. Se for não orientado, adiciona a aresta nos dois sentidos.
- **Linha 38:** Chama a função para encontrar o caminho Hamiltoniano.
- **Linhas 39-42:** Imprime o caminho encontrado ou uma mensagem informando que não existe caminho Hamiltoniano.

### Exemplo de Entrada e Saída

**Entrada (input.txt):**
```
3 3 0
0 1
1 2
0 2
```

**Saída:**
```
0 1 2
```

Se não houver caminho Hamiltoniano, a saída será:
```
Não existe caminho Hamiltoniano
```

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado no sistema

### Instruções de Execução

1. **Crie um arquivo de entrada** (ex: `input.txt`) com o grafo no formato:
   ```
   n m d
   u1 v1
   u2 v2
   ...
   um vm
   ```
   Onde:
   - `n`: número de vértices (0 a n-1)
   - `m`: número de arestas
   - `d`: 0 para não orientado, 1 para orientado
   - cada linha `ui vi` representa uma aresta

2. **Execute o programa no terminal:**
   ```zsh
   python3 main.py < input.txt
   ```
   Ou, para entrada manual:
   ```zsh
   python3 main.py
   ```
   Digite todas as linhas e pressione Ctrl+D ao final.

### Saída Esperada
- Se existir caminho Hamiltoniano: imprime a sequência de vértices.
- Se não existir: imprime `Não existe caminho Hamiltoniano`.

## Relatório Técnico

### Classes de Complexidade: P, NP, NP-Completo e NP-Difícil

1. **Em qual classe o problema do Caminho Hamiltoniano se enquadra?**
   - O problema do Caminho Hamiltoniano pertence à classe **NP-Completo**.

2. **Justificativa:**
   - **Classe P:** Problemas que podem ser resolvidos em tempo polinomial. O Caminho Hamiltoniano não possui algoritmo conhecido de tempo polinomial.
   - **Classe NP:** Problemas para os quais, dada uma solução candidata, é possível verificar se ela é válida em tempo polinomial. Se alguém fornecer um caminho, é fácil checar se ele é Hamiltoniano.
   - **Classe NP-Completo:** Problemas que estão em NP e para os quais qualquer outro problema em NP pode ser reduzido a ele em tempo polinomial. O Caminho Hamiltoniano é NP-Completo porque:
     - Está em NP (verificação rápida)
     - É tão difícil quanto qualquer outro problema em NP (há reduções conhecidas, por exemplo, do Problema do Caixeiro Viajante sem pesos)
   - **Classe NP-Difícil:** Problemas pelo menos tão difíceis quanto os NP-Completos, mas não necessariamente em NP (exemplo: Problema do Caixeiro Viajante com pesos e busca do menor caminho).

   - **Relação com o Problema do Caixeiro Viajante (PCV):**
     - O PCV é uma generalização do Caminho Hamiltoniano: se todos os pesos das arestas forem iguais, encontrar um ciclo Hamiltoniano mínimo no PCV equivale a encontrar um ciclo Hamiltoniano simples.
     - Ambos são NP-Completo (decidir se existe um caminho/ciclo Hamiltoniano) e NP-Difícil (otimização do menor caminho/ciclo).

### Análise da Complexidade Assintótica de Tempo

1. **Complexidade Temporal do Algoritmo:**
   - O algoritmo de busca por Caminho Hamiltoniano possui complexidade de tempo **O(n!)** (fatorial), onde n é o número de vértices do grafo.

2. **Justificativa e Método Utilizado:**
   - A complexidade foi determinada por **expansão da recorrência** e análise do número de operações realizadas pelo algoritmo.
   - A cada passo, o algoritmo tenta todos os vértices ainda não visitados como próximo vértice do caminho. No pior caso, para n vértices, o número de caminhos possíveis é n! (fatorial de n), pois cada permutação dos vértices pode ser um caminho potencial.
   - A recorrência que descreve o algoritmo é:
     - T(n) = n × T(n-1) + O(n)
   - Expandindo essa recorrência:
     - T(n) = n × (n-1) × T(n-2) + ...
     - No limite, T(n) = O(n!)
   - O Teorema Mestre **não se aplica** aqui, pois o problema não é dividido em subproblemas de tamanho fixo, mas sim em todos os subconjuntos possíveis de vértices restantes.
   - Portanto, a análise é feita por contagem de operações e expansão da recorrência, levando à conclusão de que o algoritmo é exponencial e cresce muito rapidamente com o aumento de n.

### Análise dos Casos de Complexidade

1. **Diferenças entre pior caso, caso médio e melhor caso:**
   - **Pior caso:** O algoritmo precisa explorar todas as possíveis permutações de vértices (n!), pois não existe caminho Hamiltoniano ou ele só é encontrado na última tentativa. Complexidade: **O(n!)**.
   - **Caso médio:** Em média, o algoritmo pode encontrar um caminho Hamiltoniano após explorar uma fração das permutações possíveis, mas ainda assim o crescimento é exponencial. Não há garantia de encontrar rapidamente, pois depende da estrutura do grafo e da ordem dos vértices. Complexidade: **O(k·n!)**, onde k < 1, mas ainda exponencial.
   - **Melhor caso:** O caminho Hamiltoniano é encontrado logo nas primeiras tentativas (por exemplo, o primeiro vértice inicial já gera um caminho válido). Complexidade: **O(n^2)**, pois percorre cada vértice e suas arestas apenas uma vez.

2. **Impacto dessas diferenças no desempenho:**
   - No **melhor caso**, o algoritmo é muito eficiente, pois encontra rapidamente a solução e termina cedo.
   - No **caso médio**, o desempenho é ruim para grafos grandes, pois o número de caminhos a serem testados cresce rapidamente, mesmo que não precise testar todos.
   - No **pior caso**, o desempenho é inviável para grafos com mais de 20 vértices, pois o tempo de execução cresce de forma fatorial.
   - Portanto, o algoritmo é prático apenas para grafos pequenos ou para instâncias em que se espera que o caminho Hamiltoniano seja encontrado rapidamente.

### Aplicação do Teorema Mestre

O Teorema Mestre é utilizado para resolver recorrências do tipo:

```
T(n) = aT(n/b) + f(n)
```

onde:
- `a` = número de subproblemas
- `n/b` = tamanho de cada subproblema
- `f(n)` = custo fora das chamadas recursivas

**No caso do algoritmo do Caminho Hamiltoniano:**
- O algoritmo testa todas as permutações possíveis de vértices, ou seja, sua recorrência não segue o padrão do Teorema Mestre.
- A recorrência típica é:
  - T(n) = n × T(n-1) + O(n)
- Isso ocorre porque, a cada passo, o algoritmo tenta todos os vértices restantes como próximo passo, não dividindo o problema em subproblemas de tamanho fixo (n/b).

**Portanto:**
- **Não é possível aplicar o Teorema Mestre** diretamente ao algoritmo do Caminho Hamiltoniano, pois ele não se encaixa na forma exigida pelo teorema (divisão em subproblemas de tamanho fixo e quantidade fixa).
- O Teorema Mestre é mais adequado para algoritmos do tipo "dividir para conquistar" (como mergesort, quicksort, Karatsuba, etc.), mas não para algoritmos de busca exaustiva como este.

**Resumo:**
- O algoritmo do Caminho Hamiltoniano tem complexidade O(n!), e não é possível usar o Teorema Mestre para resolver sua recorrência.
