import json
import networkx as nx
import pandas as pd

# ye'olde inits
j = json.load(open("items.json"))
j2 = []
names = []
indegs = []
g = nx.DiGraph()
h = nx.DiGraph()

# create the whole graph first and realize it's way too big to plot
for o in j:
    g.add_node(o["name"][0])
    for dep in o['dependencies']:
        g.add_edge(o["name"][0], dep)

# find the nodes with the highest in-degree
for node in g.nodes():
    names.append(node)
    indegs.append(g.in_degree(node))

# create a data frame so I don't have to hack too much
df = pd.DataFrame({"name": names, "indeg": indegs})
# filtering to get the top 50
s = df.sort_values('indeg', ascending=False)["name"][:50]

# getting top 50 from the first json array and all its dependencies
for i in s:
    j2 += [x for x in j if x['name'][0] == i]

# show dependencies
for o in j2:
    h.add_node(o["name"][0])
    for dep in o['dependencies']:
        h.add_edge(o["name"][0], dep)

# make .dot file and use fdp to get the graph, color at your own peril,
# just too lazy at this point
nx.nx_agraph.write_dot(h, '../out/h.dot')
