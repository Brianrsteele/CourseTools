import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import difflib


# Remove strong tags because the test html output had them removed
def remove_strong_tags(self, text):
    text = text.replace("<strong>", "")
    text = text.replace("</strong>", "")
    return text


# Read a file to use as test data
def read_test_document(document_name):
    test_document = ""
    document_name = "./src/tests/test-documents/" + document_name
    with open(document_name, "r") as the_document:
        test_document = the_document.read()
    return test_document


# strip the text of tabs, spaces, newlines, and strong tags
# to make it easier to compare strings...
def clean_text(text):
    text = text
    text = text.replace("<strong>", "")
    text = text.replace("</strong>", "")
    text = text.replace("\n\n", " ")
    text = text.replace("\n", " ")
    text = text.replace("    ", "")
    text = text.replace("        ", "")
    text = text.strip()
    return text


# return the diff of two strings
def diff_samples(str1, str2):
    list1 = str1.splitlines()
    list2 = str2.splitlines()
    d = difflib.Differ()
    diff = d.compare(list1, list2)
    diff = "\n".join(diff)
    return diff


# print a readable output
def print_diff(str1, str2):
    diff = diff_samples(str1, str2)
    print("\n\n--------------------")
    print(diff)
    print("\n\n--------------------")
