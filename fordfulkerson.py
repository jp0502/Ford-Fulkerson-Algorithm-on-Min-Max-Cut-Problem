import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

edges = pd.DataFrame({'from':['S', 'S', 'S', 'A', 'A', 'A', 'B', 'B', 'C', 'D', 'D', 'E', 'E', 'F', 'F'], 
                      'to':  ['A', 'B', 'C', 'D', 'E', 'B', 'E', 'C', 'F', 'T', 'E', 'F', 'T', 'T', 'B'], 
                    'weights':[10,  5,  15,   9,   15,  4,   8,   4,   16,  10,  15,  15,  10,  10,  6]
                           })
#show edges and weights:
edges

graph = nx.DiGraph()
for i, row in edges.iterrows():
    graph.add_edge(row[0], row[1], weight=row[2])
# graph.edges(data=True)
graph.edges(data=True)

graph.add_node('S',pos=(0,1))
graph.add_node('A',pos=(1,2))
graph.add_node('B',pos=(1,1))
graph.add_node('C',pos=(1,0))
graph.add_node('D',pos=(2,2))
graph.add_node('E',pos=(2,1))
graph.add_node('F',pos=(2,0))
graph.add_node('T',pos=(3,1))
graph.nodes(data=True)

weight = nx.get_edge_attributes(graph,'weight') 
position = nx.get_node_attributes(graph,'pos')
nx.draw(graph,position, with_labels=True)
nx.draw_networkx_edge_labels(graph,position,edge_labels = weight)
plt.show()

pip install ortools
from ortools.sat.python import cp_model
flow_model = cp_model.CpModel() 
#import the solver cp_model,and name our model flow_model

variables = {}
for edge in graph.edges:
    variables[edge[0], edge[1]] = flow_model.NewIntVar(0,152,'edge_%s_%s' % edge)
    print('Decision variable: ', variables[edge[0], edge[1]], 
          'for edge:', (edge[0], edge[1]))
    
    flow = flow_model.NewIntVar(0,152,'flow')

for node in graph.nodes:
    in_edges = graph.in_edges(node)
    out_edges = graph.out_edges(node)
    print('total constraint on node:', node)
    edge_sum = sum(variables[edge[0], edge[1]] for edge in in_edges) - sum(edge_int_vars[edge[0], edge[1]] for edge in out_edges)
    if(node == 'S'):
        flow_model.Add(edge_sum == -flow)
        print(edge_sum == -flow)
    elif(node == 'T'):
        flow_model.Add(edge_sum == flow)
        print(edge_sum == flow)
    else:
        flow_model.Add(edge_sum == 0)
        print(edge_sum, '== 0')
        
        
for edge in graph.edges:
    print('Constraint on: ', edge)
    maxflow = graph.get_edge_data(*edge)['weight']
    flow_model.Add(variables[edge[0], edge[1]] <= maxflow)
    print(variables[edge[0], edge[1]] <= maxflow)
    
    
flow_model.Maximize(flow)

maximization_solver = cp_model.CpSolver()
printer = cp_model.ObjectiveSolutionPrinter()
status = maximization_solver.SolveWithSolutionCallback(flow_model, printer)