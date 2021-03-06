from fsplit.filesplit import FileSplit
import os
from django.conf import settings

def split_file(file_to_split, number_of_chunks):
    file_size = os.path.getsize(file_to_split)
    split_size = file_size/(number_of_chunks-1)
    splitted_file_path = os.path.join(settings.MEDIA_ROOT, "splitted_file")
    # os.makedirs(splitted_file_path)
    fs = FileSplit(file_to_split, split_size, splitted_file_path)

    try:
        fs.split()
        os.remove(file_to_split)
    except e as Exception:
        print(e)
        return False
    else:
        return splitted_file_path