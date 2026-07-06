import streamlit as st

from btree import BTree
from graph import gerar_grafo

st.set_page_config(
    page_title="Visualizador de B-Tree",
    layout="wide"
)

st.title("Visualizador de B-Tree")

# Cria a árvore apenas uma vez
if "btree" not in st.session_state:
    st.session_state.btree = BTree(3)

B = st.session_state.btree

# Barra lateral
st.sidebar.header("Operações")

valor = st.sidebar.number_input(
    "Valor",
    step=1,
    value=0
)

if st.sidebar.button("Inserir"):
    B.insert(valor)

if st.sidebar.button("Remover"):
    B.delete(B.root, valor)

if st.sidebar.button("Limpar"):
    st.session_state.btree = BTree(3)
    B = st.session_state.btree

# Desenha a árvore
st.subheader("Estrutura da B-Tree")

st.graphviz_chart(gerar_grafo(B), use_container_width=True)