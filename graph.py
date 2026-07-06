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

        # Monta o texto do nó
        if len(no.keys) == 0:
            label = "{}"
        else:
            label = "{{ " + " | ".join(str(k) for k in no.keys) + " }}"

        dot.node(meu_id, label)

        # Desenha os filhos
        for filho in no.child:
            filho_id = adicionar_no(filho)
            dot.edge(meu_id, filho_id)
        
        #print(label)
        
        return meu_id
    

    adicionar_no(btree.root)
    
    #print(dot.source)

    return dot