import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files_dir = os.path.join(BASE_DIR, "files")

os.makedirs(files_dir,exist_ok=True)

my_files = range(1,5)

for i in my_files:
    fname = f"file{i}.txt"
    file_path = os.path.join(files_dir, fname)
    if os.path.exists(file_path):
        continue
    with open(file_path, 'w') as f:
        f.write(f"Hello, Welcome to file{i}")