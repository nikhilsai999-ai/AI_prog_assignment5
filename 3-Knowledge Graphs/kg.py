from rdflib import Graph, URIRef, Literal, Namespace
import networkx as nx
import matplotlib.pyplot as plt

g = Graph()

ex = Namespace("http://college.org/")

g.add((ex.Student, ex.enrolledIn, ex.AI))
g.add((ex.AI, ex.belongsTo, ex.CSE))
g.add((ex.Professor, ex.teaches, ex.AI))
g.add((ex.CSE, ex.type, Literal("Department")))

print("Knowledge Graph Relationships:\n")

for s, p, o in g:
    print(s.split("/")[-1], "->", p.split("/")[-1], "->", o.split("/")[-1])

tools = [
    "Neo4j",
    "Protégé",
    "Apache Jena",
    "RDFLib",
    "GraphDB"
]

print("\nTools Used for Building Knowledge Graphs:\n")

for t in tools:
    print(t)

G = nx.DiGraph()

for s, p, o in g:
    s_name = s.split("/")[-1]
    p_name = p.split("/")[-1]
    o_name = o.split("/")[-1]

    G.add_node(s_name)
    G.add_node(o_name)
    G.add_edge(s_name, o_name, label=p_name)

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=10
)

edge_labels = nx.get_edge_attributes(G, 'label')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

plt.title("Knowledge Graph")
plt.show()