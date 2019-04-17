import os

def make_hundred_nodes():
    try:
        os.makedirs('./nodes')
        for node in range(100):
            try:
                os.makedirs('./nodes/'+str(node+1))
            except OSError:
                return OSError
        return True
    except OSError:
        return False

print(make_hundred_nodes())