import os
import shutil
from django.conf import settings

def color_nodes():
    nodes = {}
    for node in range(100):
        nodes[node + 1] = True
    return nodes

def new_color(colored_nodes):
    nodes = {}
    for node in range(100):
        nodes[node + 1] = True
    
    for colored_node in colored_nodes:
        nodes[int(colored_node)] = False

    return nodes

def place_fragments(from_dir, t):
    nodes = color_nodes()
    files = os.listdir(from_dir)
    files.sort
    stored = []
    node = 1
    for file in files:
        file_path = os.path.join(from_dir, file)
        while nodes[node] == False:
            node+=1
        destination = os.path.join(os.path.join(settings.BASE_DIR,'nodes'), str(node))
        shutil.copy(file_path, destination)
        stored.append(destination)
        for t_value in t:
            nodes[node+t_value] = False
        node += 1
    return stored

def replicate_fragments(from_dir, t, colored_nodes):
    nodes = new_color(colored_nodes)
    files = os.listdir(from_dir)
    files.sort
    replicated = []
    node = 1
    for file in files:
        file_path = os.path.join(from_dir, file)
        while nodes[node] == False:
            node+=1
        destination = os.path.join(os.path.join(settings.BASE_DIR,'nodes'), str(node))
        shutil.move(file_path, destination)
        replicated.append(destination)
        for t_value in t:
            nodes[node+t_value] = False
        node += 1
    return replicated