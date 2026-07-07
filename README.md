
# Visualizador Interativo de Árvore B

Aplicação desenvolvida em Python para visualização e manipulação de uma **Árvore B (B-Tree)**, permitindo acompanhar graficamente as operações de inserção, remoção e busca de chaves.

O projeto utiliza **Streamlit** para construção da interface interativa e **Graphviz** para representação visual da estrutura da árvore, incluindo os nós, suas chaves e seus relacionamentos.

---

## Funcionalidades

* Criação de uma Árvore B com ordem configurável.
* Inserção de novas chaves.
* Remoção de chaves.
* Busca de elementos.
* Visualização gráfica dinâmica da árvore.
* Exibição dos espaços vazios disponíveis em cada nó.
* Sistema de logs detalhando os processos internos realizados.
* Estatísticas básicas da árvore.

---

## Tecnologias utilizadas

* **Python 3**
* **Streamlit**
  Interface gráfica interativa.
* **Graphviz**
  Geração da representação visual da árvore.

---

## Estrutura do projeto

```
ArvoreB/
│
├── app.py
├── btree.py
├── graph.py
├── requirements.txt
└── README.md
```

### `btree.py`

Contém a implementação da Árvore B:

* Estrutura dos nós.
* Inserção de chaves.
* Divisão de nós.
* Busca.
* Remoção.
* Balanceamento após remoções.
* Sistema interno de logs.

---

### `graph.py`

Responsável pela conversão da Árvore B para uma estrutura compatível com Graphviz.

Realiza:

* Criação dos nós visuais.
* Representação das chaves.
* Exibição dos espaços disponíveis.
* Conexão entre pais e filhos.

---

### `app.py`

Interface principal da aplicação utilizando Streamlit.

Responsável por:

* Entrada de chaves.
* Controle das operações.
* Escolha da ordem da árvore.
* Exibição gráfica.
* Apresentação dos logs.

---

# Instalação

## 1. Clone o repositório

```bash
git clone <url-do-repositorio>
```

Acesse a pasta:

```bash
cd ArvoreB
```

---

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não exista, instale manualmente:

```bash
pip install streamlit graphviz
```

---

## 3. Instalação do Graphviz

Além da biblioteca Python, é necessário instalar o programa Graphviz.

### Windows

Baixe pelo site oficial:

https://graphviz.org/download/

Após a instalação, adicione o caminho do Graphviz ao PATH do sistema.

Teste:

```bash
dot -V
```

O terminal deve retornar a versão instalada.

---

# Execução

Execute:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador.

Caso necessário, acesse:

```
http://localhost:8501
```

---

# Conceitos implementados

## Árvore B

Uma Árvore B é uma estrutura de dados balanceada utilizada principalmente em sistemas de armazenamento e bancos de dados.

Características:

* Todos os nós folha estão no mesmo nível.
* Cada nó possui múltiplas chaves.
* A quantidade de chaves depende da ordem configurada.
* Operações possuem custo logarítmico:

[
O(log_n)
]

---

## Ordem da árvore

A aplicação permite configurar a ordem da Árvore B.

Para uma árvore de ordem `m`:

* Cada nó pode possuir no máximo:

```
m - 1 chaves
```

* Cada nó pode possuir no máximo:

```
m filhos
```

Exemplo:

Uma Árvore B de ordem 3 possui:

```
Máximo de filhos: 3
Máximo de chaves: 2
```

Representação:

```
        [10 | 20]

      /     |      \

 [1]     [15]    [30]
```

---

# Sistema de Logs

A aplicação possui um sistema de acompanhamento das operações internas.

Exemplo de inserção:

```
Iniciando inserção da chave 25.
Nó folha encontrado.
Inserindo a chave 25.
O nó excedeu o número máximo de chaves.
Realizando divisão.
A chave 20 será promovida.
Inserção concluída.
```

Isso permite observar:

* Descidas na árvore.
* Divisões de nós.
* Promoção de chaves.
* Empréstimos entre irmãos.
* Fusões durante remoções.

---

# Exemplo de utilização

Inserindo:

```
10,20,5,6,12,30,7,17
```

A árvore gerada será semelhante:

```
              [10 | 20]

          /       |        \

      [5|6|7]   [12|17]   [30]
```

---

# Objetivo

O objetivo deste projeto é auxiliar no estudo e compreensão do funcionamento de Árvores B, permitindo visualizar de forma intuitiva os processos normalmente abstratos apresentados em disciplinas de Estrutura de Dados e Banco de Dados.

---

# Autor

Desenvolvido por:

**Guilherme Muniz de Oliveira Reis**

Projeto acadêmico para estudo e visualização de estruturas de dados.
