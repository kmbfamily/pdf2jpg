import os
from pdf2image import convert_from_path

file_path = os.getcwd()
file_names = os.listdir(file_path)
for name in file_names:
    if name.endswith(".pdf"):
        images = convert_from_path(pdf_path=name,dpi=400,poppler_path='poppler\\Library\\bin')
        for i, page in enumerate(images,start=1):
            page.save(name.replace('.pdf','')+'_'+str(i)+'.jpg',"JPEG")
