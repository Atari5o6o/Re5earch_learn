#code to plot the knowledge graph of the entities and relationships extracted from the paper
#in relationships.py
import networkx as nx
import matplotlib.pyplot as plt
import relationships
from relationships import entities, relationships



# Process the paper text to extract entities and relationships
# (Assuming you have already performed entity extraction and relationship extraction)


# Create a directed graph
graph = nx.DiGraph()

# Add entities as nodes to the graph
for entity, label in entities:
    graph.add_node(entity, label=label)

# Add relationships as edges to the graph
for relationship, entities_involved in relationships:
    for entity in entities_involved:
        graph.add_edge(entity, relationship)

# Set node positions for better visualization layout
pos = nx.spring_layout(graph)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx(graph, pos, with_labels=True, node_size=800, font_size=10, font_weight='bold', node_color='lightblue', edge_color='gray')
plt.title('Scientific Paper Knowledge Graph')
plt.axis('off')
plt.show()
