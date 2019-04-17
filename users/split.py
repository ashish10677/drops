from fsplit.filesplit import FileSplit
# import filemerge
import os
from django.conf import settings

def split_file(file_to_split, number_of_chunks):
    print("---------------------Start split---------------------")
    file_size = os.path.getsize(file_to_split)
    split_size = file_size/(number_of_chunks-1)
    
    fs = FileSplit(file_to_split, split_size, settings.MEDIA_ROOT)

    try:
        fs.split()
    except e as Exception:
        print("---------------------Failed to split the file---------------------")
        print(e)
    else:
        print("Splitted file into",number_of_chunks,"chunks")

# 'print("---------------------Start merging---------------------")
# merge = input("Enter the name of merged file: ")
# try: 
#     filemerge.join(output_dir, merge)
# except e as Exception:
#     print("---------------------Failed to merge the file---------------------")
#     print(e)
# else:
#     print("Merged file into", merge)


