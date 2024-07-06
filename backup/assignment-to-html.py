import markdown
import re
import tkinter as tk
from tkinter import filedialog
import os

# trying to just convert to html in the simplest way possible.

# ------------------------------- Functions ----------------------------------

def import_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# ------------------ FILE IO Functions -----------------------------

# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

# ------------------ Document Functions ----------------------------

def find_section(sections_list, section_name):
    matching_sections = \
        [section for section in sections_list if section.startswith(section_name)]
    return matching_sections[0]

def find_document_title(sections_list):
    title = find_section(sections_list,"# ")
    title = title[2:]
    return title

def parse_sections(text):
    # split on "## " to find h2 headers and get rid of space
    return text.split("## ")

# ------------------ Section Functions -----------------------------

def remove_bold(text):
    clean_text = text.replace("**", "")
    return clean_text

def detect_asterisks(text):
    if "*" in text:
        return True
    else:
        return False

def find_section_title(section):
    title = section.split("\n\n")[0]
    title = "##" + title
    return title

def find_section_content(section):
    content = section.split("\n\n")[1:]
    content = '\n\n'.join(content)
    return content

def process_section(section):
    # define the parts of the section
    title = find_section_title(section)
    content = find_section_content(section)
    
    # process the section in ways that
    # are easiest if the text is in markdown
    content = remove_bold(content)
    processed_section = title + "\n\n" + content
    processed_section = markdown.markdown(processed_section, extensions=['tables'])

    # process the section in ways that need to
    # be done on HTML text
    processed_section = make_tables_pretty(processed_section)
    return processed_section

# Has some html code generation mixed in...
def process_gallery_section(section):
    # temporarily change the images while testing.
    gallery = make_temp_images(section)
    gallery = process_section(gallery)
    title = find_section_title(section)[2:]
    title = "<h2>" + title + "</h2>\n"
    gallery = make_image_gallery(gallery)
    gallery_output = ""
    gallery_output += title + "\n"
    for figure in gallery:
        gallery_output += figure
    return gallery_output

def generate_section_title_list(sections_list):
    section_title_list = []
    for section in sections_list:
        title = find_section_title(section)
        title = title[2:]
        section_title_list.append(title)
    return section_title_list[1:]

# ------------------ HTML OutPut Functions --------------------------
  
def make_temp_images(text):
    text = re.sub('\(.*\)', '(test.jpg)', text)
    return text

def make_images_responsive(text):
    text = re.sub('(<img)', '<img class="img-fluid figure-img img-fluid rounded"', text)
    return text

def make_tables_pretty(text):
    text = re.sub('(<table)', '<table class="table table-striped"', text)
    return text

def make_image_gallery(text):
    gallery_items = text.split("<li>")
    figure_list = []
    figure = ""
    for image in gallery_items[1:]:
        image = make_images_responsive(image)
        image = image.replace("\n", "")
        image = image.replace("</li>", "")
        image = image.replace("</ul>", "")
        
        completed_flag = False
        if "<img" in image:
            figure += "<figure class=\"figure\">\n"
            figure += image + "\n"
        else:
            figure += "<figcaption class=\"figure-caption text-end\">\n"
            figure += image + "\n"
            figure += "</figcaption >\n"
            figure += "</figure>\n"
            completed_flag = True
           
        if completed_flag is True:
            figure_list.append(figure)
            completed_flag = False
            figure = ""
    return figure_list

def process_html_content(sections_list):
    section_title_list = generate_section_title_list(sections_list)
    
    title = find_document_title(sections_list)
    title = "<h1>" + title + "</h1>\n"

    html_content = title

    for section_title in section_title_list:
        section = find_section(sections_list, section_title)
        if section_title == "Student Examples" \
                or section_title == "Real World Examples":
            section = process_gallery_section(section)
        else:
            section = process_section(section)
        html_content += section
    
    return html_content

def create_html_header(sections_list):
    output_string = ""
    output_string += "<!DOCTYPE html>\n"
    output_string += "<html lang=\"en\">\n"
    output_string += "<head>\n"
    output_string += "    <meta charset=\"UTF-8\">\n"
    output_string += "    <meta name=\"viewport\" content=\"width=device-width,"
    output_string += "initial-scale=1.0\">\n"
    output_string += "    <title>" + find_document_title(sections_list) + "</title>\n"
    output_string += "     <link href=\""
    output_string += "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min."
    output_string += "css\" rel=\"stylesheet\" integrity=\""
    output_string += " sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW"
    output_string += "+ALE"
    output_string += "wIH\" crossorigin=\"anonymous\">"
    output_string += "</head>\n"
    output_string += "<body>\n"
    output_string += "<div class=\"container-md\">"
    return output_string

def create_html_footer():
    output_string = ""
    output_string += "</div>"
    output_string += "<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/"
    output_string += "bootstrap.bundle.min.js\" integrity=\"sha384-"
    output_string += "YvpcrYf0tY3lHB60NNkmXc5"
    output_string += "s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz\" crossorigin="
    output_string += "\"anonymous\"></script>\n"
    output_string += "</body>\n"
    output_string += "</html>"
    return output_string

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

with open(file_path, 'r') as file:
    assignment_text = file.read() 

# ------------------------------------------------- Process the article ---------------
sections_list = parse_sections(assignment_text)  

# create an html output string
output_string = create_html_header(sections_list)
output_string += process_html_content(sections_list)
output_string += create_html_footer()

# ----------------------------------------------- Save the HTML file ------

with open(html_file_path, 'w') as file:
    file.write(output_string)