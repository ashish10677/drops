import os, sys, shutil
from django.conf import settings

def join(fromdir, tofile):
    print("From Directory", fromdir)
    print("To file", tofile)
    readsize = 1024
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        os.remove(filepath)

def get_all_chunks(node_list, file_name):
    node_root = os.path.join(settings.BASE_DIR, 'nodes')
    for node in node_list:
        chunk_name = file_name.split('.')[0]+"_"+str(node_list.index(node)+1)+"."+file_name.split(".")[1]
        chunk = os.path.join(node_root, node, chunk_name)
        destination = os.path.join(settings.BASE_DIR, 'media', 'splitted_file')
        shutil.copy(chunk, destination)
    join(destination, file_name)
