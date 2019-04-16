from fsplit.filesplit import FileSplit
import filemerge
import os

print("---------------------Start split---------------------")
file_to_split = input("Enter the full path of the file to be split: ")
output_dir = input("Enter the output directory: ")
number_of_chunks = int(input("Enter the number of chunks: "))
file_size = os.path.getsize(file_to_split)
split_size = file_size/(number_of_chunks-1)

fs = FileSplit(file_to_split, split_size, output_dir)

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


