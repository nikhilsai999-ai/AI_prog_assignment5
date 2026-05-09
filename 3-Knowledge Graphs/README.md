Knowledge Graph Implementation using RDFLib – Documentation and README

Introduction

This project demonstrates the implementation and visualization of a Knowledge Graph (KG) using Python.

A Knowledge Graph is a structured representation of information where:

* Entities are represented as nodes
* Relationships are represented as edges

Knowledge Graphs are widely used in:

* Artificial Intelligence
* Semantic Web
* Search Engines
* Recommendation Systems
* Chatbots
* Healthcare Systems
* Education Platforms

This project uses:

* RDFLib for RDF graph creation
* NetworkX for graph representation
* Matplotlib for graph visualization

Objective

The objective of this project is to:

* Understand the concept of Knowledge Graphs
* Represent entities and relationships using RDF triples
* Visualize graph-based relationships
* Explore tools used to build Knowledge Graphs
* Demonstrate semantic relationships between entities

Knowledge Graph

A Knowledge Graph is a graph-based data structure that stores information in the form of:

Subject → Predicate → Object

This structure is called an RDF Triple.

Example:

Student → enrolledIn → AI

Here:

* Student = Subject
* enrolledIn = Predicate
* AI = Object

Knowledge Graphs help machines understand relationships between entities.

Features of Knowledge Graphs

* Stores structured semantic information
* Represents relationships clearly
* Supports intelligent querying
* Improves data linking
* Enables reasoning and inference

Applications of Knowledge Graphs

* Google Search Knowledge Panel
* ChatGPT and AI Assistants
* Recommendation Systems
* Fraud Detection
* Healthcare Systems
* Educational Platforms
* Social Networks

Concepts Used

RDF (Resource Description Framework)

RDF is a standard model used to represent data in the Semantic Web.

Data is represented as triples:

* Subject
* Predicate
* Object

Example:
Student → enrolledIn → AI

URI (Uniform Resource Identifier)

URIs uniquely identify entities.

Example:
[http://college.org/Student](http://college.org/Student)

Namespace

A namespace helps avoid naming conflicts by defining a common URI prefix.

Example:

ex = Namespace("[http://college.org/](http://college.org/)")

Graph Representation

The graph stores:

* Nodes → Entities
* Edges → Relationships

Code Explanation

Import Statements

from rdflib import Graph, URIRef, Literal, Namespace
import networkx as nx
import matplotlib.pyplot as plt

Purpose:
Imports required libraries.

Libraries Used

RDFLib

* Used for creating RDF graphs
* Handles semantic triples

NetworkX

* Used for graph representation

Matplotlib

* Used for graph visualization

Creating RDF Graph

g = Graph()

Purpose:
Creates an empty RDF graph.

Creating Namespace

ex = Namespace("[http://college.org/](http://college.org/)")

Purpose:
Defines a namespace for entities.

This allows creation of semantic URIs like:

* ex.Student
* ex.AI
* ex.CSE

Adding RDF Triples

g.add((ex.Student, ex.enrolledIn, ex.AI))

Purpose:
Adds relationship:
Student → enrolledIn → AI

Other Relationships

g.add((ex.AI, ex.belongsTo, ex.CSE))

Represents:
AI → belongsTo → CSE

g.add((ex.Professor, ex.teaches, ex.AI))

Represents:
Professor → teaches → AI

g.add((ex.CSE, ex.type, Literal("Department")))

Represents:
CSE → type → Department

Literal

Literal values store actual text data instead of URI references.

Example:
Literal("Department")

Printing Relationships

for s, p, o in g:
print(s.split("/")[-1], "->", p.split("/")[-1], "->", o.split("/")[-1])

Purpose:
Displays graph triples in readable format.

Output Example

Student -> enrolledIn -> AI
AI -> belongsTo -> CSE
Professor -> teaches -> AI
CSE -> type -> Department

Tools Used for Building Knowledge Graphs

The program includes some popular Knowledge Graph tools:

Neo4j

* Graph database platform
* Uses Cypher query language
* Popular for graph analytics

Protégé

* Ontology editor
* Used for Semantic Web applications

Apache Jena

* Java framework for RDF and SPARQL

RDFLib

* Python library for RDF handling

GraphDB

* Semantic graph database platform

Tools List in Code

tools = [
"Neo4j",
"Protégé",
"Apache Jena",
"RDFLib",
"GraphDB"
]

Graph Visualization

Creating Directed Graph

G = nx.DiGraph()

Purpose:
Creates a directed graph using NetworkX.

Adding Nodes and Edges

G.add_node(s_name)
G.add_node(o_name)
G.add_edge(s_name, o_name, label=p_name)

Purpose:

* Adds entities as nodes
* Adds relationships as edges

Graph Layout

pos = nx.spring_layout(G)

Purpose:
Automatically positions nodes.

Drawing Graph

nx.draw(
G,
pos,
with_labels=True,
node_size=3000,
font_size=10
)

Purpose:
Visualizes nodes and edges.

Edge Labels

nx.draw_networkx_edge_labels(
G,
pos,
edge_labels=edge_labels
)

Purpose:
Displays relationship names on edges.

Displaying Graph

plt.title("Knowledge Graph")
plt.show()

Purpose:
Displays final graph visualization.

Graph Structure

Knowledge Graph Representation

Student ------ enrolledIn ------> AI
AI ----------- belongsTo -------> CSE
Professor ----- teaches --------> AI
CSE ----------- type -----------> Department

Expected Output

Knowledge Graph Relationships:

Student -> enrolledIn -> AI
AI -> belongsTo -> CSE
Professor -> teaches -> AI
CSE -> type -> Department

Tools Used for Building Knowledge Graphs:

Neo4j
Protégé
Apache Jena
RDFLib
GraphDB

A graph visualization window will also appear showing entity relationships.

Time Complexity

Adding Triples:
O(n)

Graph Traversal:
O(n)

Where:

* n = Number of triples

Space Complexity

O(n)

Because all graph nodes and edges are stored in memory.

Advantages

* Represents semantic relationships clearly
* Easy to visualize relationships
* Supports intelligent querying
* Useful for AI applications
* Easy to expand with more entities

Limitations

* Large graphs can become complex
* Requires semantic modeling knowledge
* Visualization becomes difficult for huge datasets

Test Cases

Test Case 1

Input Triple

Student → enrolledIn → AI

Expected Output

Student -> enrolledIn -> AI

Test Case 2

Input Triple

Professor → teaches → AI

Expected Output

Professor -> teaches -> AI

Test Case 3

Input Triple

AI → belongsTo → CSE

Expected Output

AI -> belongsTo -> CSE

Test Case 4

Input Triple

CSE → type → Department

Expected Output

CSE -> type -> Department

Conclusion

This project successfully demonstrates the implementation of a Knowledge Graph using RDFLib and NetworkX in Python.

The system:

* Represents semantic relationships using RDF triples
* Visualizes entity relationships as a graph
* Demonstrates concepts of Semantic Web and Knowledge Representation
* Explores popular tools used in Knowledge Graph development