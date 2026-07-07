from graphviz import Digraph


def gerar_grafo(btree):
	"""
	Recebe uma BTree e retorna um objeto Digraph.
	"""

	dot = Digraph("BTree")

	dot.attr(
		"node",
		shape="record",
		height=".1",
		fontname="Arial"
	)

	contador = [0]

	def adicionar_no(no):
		meu_id = f"node{contador[0]}"
		contador[0] += 1

		campos = [str(k) for k in no.keys]

		while len(campos) < btree.max_keys:
			campos.append(" ")

		label = "{{ " + " | ".join(campos) + " }}"

		if no.highlight:
			dot.node(
				meu_id,
				label,
				style="filled",
				fillcolor="lightblue"
			)
		else:
			dot.node(meu_id, label)

		for filho in no.child:
			filho_id = adicionar_no(filho)
			dot.edge(meu_id, filho_id)

		return meu_id

	adicionar_no(btree.root)

	return dot