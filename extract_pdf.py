# importing required modules
from PyPDF2 import PdfReader



all_text = ""

# creating a pdf reader object
reader = PdfReader('/Users/anmol/Developer/Implementation/A simple quantum voting scheme wih multi qubit entanglemet.pdf')
count = len(reader.pages)
for i in range(count):
    page = reader.pages[i]
    all_text += page.extract_text()


#print(all_text)
#print(abstract)