import os
import shutil
from django.conf import settings

def color_nodes():
    nodes = {}
    for node in range(100):
        nodes[node + 1] = True
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
        shutil.move(file_path, destination)
        stored.append(destination)
        for t_value in t:
            nodes[node+t_value] = False
        node += 1
    return stored