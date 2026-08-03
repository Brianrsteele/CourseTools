import pypandoc  # type: ignore

string = "# Yo, this is a Level One Header!"

pypandoc.convert_text(string, to="docx", format="md", outputfile="output.docx")
