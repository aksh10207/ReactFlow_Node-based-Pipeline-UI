from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Dict
from collections import defaultdict, deque
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:3000",  # React frontend
    # Add other origins if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods
    allow_headers=["*"],    # Allow all headers
)

class Edge(BaseModel):
    source: str
    target: str

class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(pipeline: Pipeline):
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)

    # Build adjacency list
    adj = defaultdict(list)
    for edge in pipeline.edges:
        adj[edge.source].append(edge.target)

    # Function to detect cycles using Kahn's Algorithm
    def is_dag(num_nodes, adj):
        # Calculate in-degrees
        in_degree = {node.id: 0 for node in pipeline.nodes}
        for edge in pipeline.edges:
            if edge.target in in_degree:
                in_degree[edge.target] += 1

        # Initialize queue with nodes having in-degree 0
        queue = deque([node_id for node_id, degree in in_degree.items() if degree == 0])

        visited = 0

        while queue:
            current = queue.popleft()
            visited += 1
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == num_nodes

    dag = is_dag(num_nodes, adj)

    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': dag
    }