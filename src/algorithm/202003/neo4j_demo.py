from py2neo import Graph, Node, Relationship, NodeMatcher
graph = Graph("bolt://localhost:7687", auth=("neo4j", "asdf123"))
g = graph.run("match (n:Company) where n.Com_name = '平安银行' return n")
print(g.data())
