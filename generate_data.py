import numpy as np
import pandas as pd
import networkx as nx
import random
from PIL import Image
import os

# Function to convert adjacency matrix and heatmap to fixed-size image
def convert_to_heatmap_image(G, target_size=64):
    adj_matrix = nx.to_numpy_array(G)
    matrix_size = adj_matrix.shape[0]

    if matrix_size < target_size:
        padded_matrix = np.zeros((target_size, target_size), dtype=int)
        padded_matrix[:matrix_size, :matrix_size] = adj_matrix
    elif matrix_size > target_size:
        image = Image.fromarray(adj_matrix)
        padded_matrix = np.array(image.resize((target_size, target_size), Image.BILINEAR))
    else:
        padded_matrix = adj_matrix

    degree_dict = dict(G.degree())
    degrees = np.array([degree_dict[node] for node in G.nodes()])
    heatmap = np.zeros((target_size, target_size), dtype=float)

    for i, node in enumerate(G.nodes()):
        if i < target_size:
            heatmap[i, i] = degrees[i]

    combined_matrix = padded_matrix + heatmap
    combined_image = (combined_matrix / combined_matrix.max() * 255).astype(np.uint8)

    return Image.fromarray(combined_image, 'L')

# Function to generate random graphs and calculate their independence number
def generate_independence_number_data(num_graphs, max_nodes):
    graphs = []
    independence_numbers = []
    for _ in range(num_graphs):
        num_nodes = random.randint(5, max_nodes)
        G = nx.gnp_random_graph(num_nodes, np.random.rand())
        ind_num = nx.algorithms.approximation.maximum_independent_set(G)
        graphs.append(G)
        independence_numbers.append(len(ind_num))
    return graphs, independence_numbers

# Function to save the dataset
def save_dataset(graphs, independence_numbers, target_size=64, output_dir='dataset'):
    os.makedirs(os.path.join(output_dir, 'data'), exist_ok=True)
    images = []
    for i, graph in enumerate(graphs):
        image = convert_to_heatmap_image(graph, target_size)
        image_path = os.path.join(output_dir, f'data/graph_{i}.png')
        image.save(image_path)
        images.append(np.array(image).reshape(target_size, target_size, 1))

    # Save numpy arrays
    X = np.array(images)
    y = np.array(independence_numbers)
    np.save(os.path.join(output_dir, 'X.npy'), X)
    np.save(os.path.join(output_dir, 'y.npy'), y)

# Generate and save dataset
num_graphs = 2000
max_nodes = 64
graphs, independence_numbers = generate_independence_number_data(num_graphs, max_nodes)
save_dataset(graphs, independence_numbers)

print(f"Dataset generated and saved in the dataset directory.")
