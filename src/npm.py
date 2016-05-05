import json
import networkx as nx
import pandas as pd

# ye'olde inits
j = json.load(open("items.json"))
j2 = []
t = []
g = nx.DiGraph()
h = nx.DiGraph()

# create the whole graph first and realize it's way too big to plot
for o in j:
    for dep in o['dependencies']:
        g.add_edge(o["name"][0], dep)

# find the nodes with the highest degree centrality
for k, v in nx.in_degree_centrality(g).iteritems():
    t.append((k, v))

# create a data frame so I don't have to hack too much
df = pd.DataFrame(t)
# totally unnecessary filtering to get the top 50
# I could have just sorted the values....
s = df[df[1] > df.quantile(0.99965).max()][0].values

# getting top 50 from the first json array and all its dependencies
for i in s:
    j2 += [x for x in j if x['name'][0] == i]

# show dependencies
for o in j2:
    for dep in o['dependencies']:
        h.add_edge(o["name"][0], dep)

# mask dependencies
# for i, o in enumerate(j2):
#     for j, dep in enumerate(o['dependencies']):
#         h.add_edge(o["name"][0], str(i)+str(j))

# make .dot file and use fdp to get the graph, color at your own peril,
# just too lazy at this point
nx.nx_agraph.write_dot(h, 'h.dot')
