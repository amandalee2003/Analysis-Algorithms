#!/usr/bin/env python3

import sys 

class DisjointSet:
    def __init__(self, state):
        self.parent = list(range(state))
        self.rank = [0] * state

    def find(self, state):
        if self.parent[state] != state:
            self.parent[state] = self.find(self.parent[state])
        return self.parent[state]

    def union(self, state_1, state_2):
        root_1 = self.find(state_1)
        root_2 = self.find(state_2)
        if root_1 != root_2:
            if self.rank[root_1] > self.rank[root_2]:
                self.parent[root_2] = root_1
            elif self.rank[root_1] < self.rank[root_2]:
                self.parent[root_1] = root_2
            else:
                self.parent[root_2] = root_1
                self.rank[root_1] = self.rank[root_1] + 1

def kruskal_algor(num, edges):
    edges.sort(key=lambda x: x[2])
    dis = DisjointSet(num)
    minSpanTree = []
    total_weight = 0.0
    for edge in edges:
        i, j, weight, label = edge
        if dis.find(i) != dis.find(j):
            dis.union(i, j)
            minSpanTree.append((label, i, j, weight))
            total_weight = total_weight + weight
    return minSpanTree, total_weight

def read_input(filename):
    with open(filename, 'r') as file:
        split1 = int(file.readline().strip())
        split2 = int(file.readline().strip())
        edges = []
        for i in range(split2):
            u, v, w = file.readline().strip().split()
            u, v, w = int(u) - 1, int(v) - 1, float(w)  # Adjust 1-based to 0-based index
            edges.append((u, v, w, i + 1))  # Adding label as i + 1
    return split1, edges

def write_output(filename, mst, total_weight):
    with open(filename, 'w') as file:
        for label, u, v, weight in mst:
            file.write(f"{label:4}: ({u + 1}, {v + 1}) {weight:.1f}\n")  # Adjust 0-based back to 1-based index
        file.write(f"Total Weight = {total_weight:.2f}\n")

def main():
    if len(sys.argv) == 3:
        input_file, output_file = sys.argv[1], sys.argv[2]
        num, edges = read_input(input_file)
        minSpanTree, total_weight = kruskal_algor(num, edges)
        write_output(output_file, minSpanTree, total_weight)


main()

