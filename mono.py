import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz'

import matplotlib.pyplot as plt
import pygraphviz as pgv
import networkx as nx

# Crear el gráfico
graph = pgv.AGraph(directed=True, strict=True)

# Agregar los actores
graph.add_node("Cliente", shape="actor")
graph.add_node("Agencia de Viajes", shape="actor")

# Agregar los casos de uso
graph.add_node("Realizar reserva de pasaje")
graph.add_node("Agregar tours asociados")
graph.add_node("Realizar pago")
graph.add_node("Emitir ticket de pasaje")

# Agregar las relaciones entre actores y casos de uso
graph.add_edge("Cliente", "Realizar reserva de pasaje")
graph.add_edge("Agencia de Viajes", "Realizar reserva de pasaje")
graph.add_edge("Cliente", "Agregar tours asociados")
graph.add_edge("Agencia de Viajes", "Agregar tours asociados")
graph.add_edge("Cliente", "Realizar pago")
graph.add_edge("Agencia de Viajes", "Realizar pago")
graph.add_edge("Cliente", "Emitir ticket de pasaje")
graph.add_edge("Agencia de Viajes", "Emitir ticket de pasaje")

# Convertir el gráfico a un objeto de red
nx_graph = graph.to_agraph().to_networkx()

# Dibujar el gráfico
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(nx_graph, seed=42)
nx.draw(nx_graph, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10, edge_color="gray")
plt.axis("off")

# Mostrar el gráfico en una ventana
plt.show()
