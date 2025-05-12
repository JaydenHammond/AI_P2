## Manto de Markov es el conjunto de nodos que hacen que un nodo sea independiente del resto de la red dado ese conjunto.
## f(n) = Padres(n) ∪ Hijos(n) ∪ Padres(Hijos(n)); con esto, P(n | resto) = P(n | f(n)).

# RECORDATORIO: defino la estructura de la red como un diccionario de padres.
# Cada clave es un nodo, y el valor es la lista de sus padres directos.
parents = {
    'Rain': [],
    'Sprinkler': ['Rain'],
    'WetGrass': ['Rain', 'Sprinkler'],
    'Season': []
}

# RECORDATORIO: genero la lista de hijos invirtiendo 'parents'.
children = {node: [] for node in parents}
for node, ps in parents.items():
    for p in ps:
        children[p].append(node)

# RECORDATORIO: función para calcular el Manto (blanket) de un nodo dado.
def markov_blanket(node):
    # Padres directos
    padres = set(parents[node])
    # Hijos directos
    hijos = set(children[node])
    # Padres de los hijos (excepto el propio nodo)
    padres_de_hijos = set()
    for h in hijos:
        for p in parents[h]:
            if p != node:
                padres_de_hijos.add(p)
    # Unión de los tres conjuntos
    return padres | hijos | padres_de_hijos

# RECORDATORIO: elijo un nodo para ejemplificar, por ejemplo 'Sprinkler'.
nodo = 'Sprinkler'
blanket = markov_blanket(nodo)

# RESULTADO: muestro el Manto de Markov de 'Sprinkler'.
print(f"\nManto de Markov de '{nodo}': {blanket}")
# RECORDATORIO: aquí obtengo padres={'Rain'}, hijos={'WetGrass'}, padres_de_hijos={'Rain'} → blanket={'Rain','WetGrass'}.
