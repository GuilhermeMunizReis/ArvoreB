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

# Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/GuilhermeMunizReis/ArvoreB.git
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

# Autor

Desenvolvido por:

**Guilherme Muniz de Oliveira Reis**

Projeto acadêmico para estudo e visualização de estruturas de dados.
