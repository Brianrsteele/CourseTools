import tkinter as tk
from tkinter import filedialog
import os
from documentModels.Document import Document

# ------------------------------- Functions ----------------------------------


def import_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


# ------------------------------------------------- Open file ----------------

file_path = import_file()
file_path_parts = os.path.split(file_path)
folder = file_path_parts[0]
markdown_filename = file_path_parts[1]
html_filename = markdown_filename.split(".")[0] + ".html"
html_file_path = folder + "/" + html_filename

# https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.geeksforgeeks.org/python-os-path-split-method/&ved=2ahUKEwirr8G7wJKGAxVghIkEHcIzCAYQFnoECBoQAQ&usg=AOvVaw1RrZFamTAalqfv1adkEIOh

print(file_path)
print(folder)
print(markdown_filename)
print(html_filename)
print(html_file_path)

with open(file_path, "r") as file:
    assignment_text = file.read()

# ------------------------------------------------- Process the article ---------------

document = Document(assignment_text)
output_html = document.render("bootstrap")

print(output_html)

with open(html_file_path, "w") as file:
    file.write(output_html)
