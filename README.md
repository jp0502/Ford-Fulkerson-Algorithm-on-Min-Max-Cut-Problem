# Ford-Fulkerson-Algorithm-on-Min-Max-Cut-Problem
This is a Ford-Fulkerson algorithm that finds the maximum flow on a network. I wrote it in Python for an extra credit assignment for a combinatorial optimization course for my program.

The FF-algorithm is a greedy algorithm that searches for the maximum amount a flow of something (network packets of data, water, electricity, car traffic, etc...) from the start to the end node of a network of nodes and paths.

It first searches for the path that can send the most amount of flow, then fills out the entire network through forward and backward flows. It ends whenever it can no longer find a path that has a non-zero capacity. 
