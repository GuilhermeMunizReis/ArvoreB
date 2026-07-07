import streamlit as st

from btree import BTree
from graph import gerar_grafo


# ==========================
# Configuração da página
# ==========================

st.set_page_config(
	page_title="Visualizador de B-Tree",
	layout="wide"
)

st.title("Visualizador de B-Tree")
st.caption("Visualização interativa de uma Árvore B utilizando Graphviz")


# ==========================
# Sessão
# ==========================

if "ordem" not in st.session_state:
	st.session_state.ordem = 3

if "btree" not in st.session_state:
	st.session_state.btree = BTree(
		st.session_state.ordem
	)


# ==========================
# Layout
# ==========================

col_controles, col_arvore = st.columns([1, 3])


# ==========================
# Controles
# ==========================

with col_controles:

	st.subheader("Operações")


	# ==========================
	# Ordem da árvore
	# ==========================

	nova_ordem = st.number_input(
		"Ordem da B-Tree",
		min_value=3,
		max_value=10,
		value=st.session_state.ordem,
		step=1
	)


	if nova_ordem != st.session_state.ordem:

		st.session_state.ordem = nova_ordem

		st.session_state.btree = BTree(
			nova_ordem
		)

		st.success(
			f"Nova B-Tree criada com ordem {nova_ordem}."
		)


	B = st.session_state.btree


	st.info(
		f"""
		**Configuração atual**

		Ordem: {B.t}

		Máximo de chaves: {B.max_keys}

		Mínimo de chaves: {B.min_keys}
		"""
	)


	valor = st.number_input(
		"Chave",
		step=1,
		value=0
	)


	st.write("")


	col1, col2 = st.columns(2)


	with col1:

		inserir = st.button(
			"➕ Inserir",
			use_container_width=True
		)


	with col2:

		remover = st.button(
			"➖ Remover",
			use_container_width=True
		)


	buscar = st.button(
		"🔍 Buscar",
		use_container_width=True
	)


	st.divider()


	limpar = st.button(
		"🗑️ Limpar",
		use_container_width=True
	)


	# ==========================
	# Estatísticas
	# ==========================

	st.divider()

	st.subheader("Estatísticas")


	c1, c2 = st.columns(2)

	c1.metric(
		"Altura",
		"-"
	)

	c2.metric(
		"Nós",
		"-"
	)


	st.metric(
		"Chaves na raiz",
		len(B.root.keys)
	)
 
	# ==========================
	# Logs
	# ==========================

	st.divider()

	st.subheader("Logs da operação")

	if len(B.logs) > 0:

		for log in B.logs:
			st.write("•", log)

	else:

		st.write("Nenhuma operação realizada.")    


# ==========================
# Operações
# ==========================

if inserir:

	if B.search(valor) is None:

		B.insert(valor)

		st.success(
			f"{valor} inserido."
		)

	else:

		st.warning(
			"Essa chave já existe."
		)


if remover:

	if B.search(valor):

		B.delete(
			B.root,
			valor
		)

		st.success(
			f"{valor} removido."
		)

	else:

		st.error(
			"Chave não encontrada."
		)


if buscar:

	if B.search(valor):

		st.success(
			"Chave encontrada."
		)

	else:

		st.error(
			"Chave não encontrada."
		)


if limpar:

	st.session_state.btree = BTree(
		st.session_state.ordem
	)

	B = st.session_state.btree


# ==========================
# Visualização
# ==========================

with col_arvore:

	st.subheader("Estrutura da Árvore")


	st.graphviz_chart(
		gerar_grafo(B),
		use_container_width=True
	)
 
