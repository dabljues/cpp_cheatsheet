import os

if os.path.isfile("cheatsheet.md"):
    os.remove("cheatsheet.md")

files = [f for f in os.listdir() if f.endswith(".md") and f != "README.md"]

with open("cheatsheet.md", "a") as f_cheatsheet:
    for filename in files:
        with open(filename, "r") as f:
            f_cheatsheet.write(f.read() + "\n")
