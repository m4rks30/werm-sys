
import os

for i in range(1, 10000):
    filename = f"file{i}.txt"
    with open(filename, "w") as f:
        f.write("Hello World")
        print(f"{filename} created.")
