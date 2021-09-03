from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
 
FILE_PATH = "./pdf/qualification_tp2021.pdf"

out = extract_pages(FILE_PATH)
 
"""
for page_layout in extract_pages(FILE_PATH):
    f = open('textput.txt', 'a')
    for element in page_layout:
        print(element)
        f.write(str(element))
    f.close
"""

for page_layout in out:
    print(page_layout)