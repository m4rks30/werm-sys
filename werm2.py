import os

def create_large_file('large_file.bin', 1024 * 1024 * 1024):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_bytes))
