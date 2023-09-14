# importing required modules
from PyPDF2 import PdfReader


pdf_file_path = '/Users/anmol/Developer/Projects/Research paper service/basics-of-calculus-simplified.pdf'
all_text = ""

# creating a pdf reader object
reader = PdfReader(pdf_file_path)
count = len(reader.pages)
for i in range(count):
    page = reader.pages[i]
    all_text += page.extract_text()


print(all_text)
#print(abstract)