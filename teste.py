import PyPDF2
import re

arquivo_path="ementa_computacao_bac.pdf" 
arquivo_aberto = PyPDF2.PdfReader(arquivo_path) 
print(f"{len((arquivo_aberto.pages))} Páginas encontradas")

#padrao = r"([\w\s]+)[,;]\s([\w\s\.&]+)\.\s([\w\s]+):\s([\w\s\.-]+),\s([\d]{4})[.;]" #um que nao funcionou muito legal
padrao=r"([\w\s]+),\s([\w\s\.&]+)\.\s([\w\s:]+)\.\s([\w\s]+):\s([\w\s\.]+),?\s([\w\s,]+)?\s*[\.;]" #funcionou mas pra menos da metade das referencias
for indice,pagina in enumerate(arquivo_aberto.pages): #Percorre as páginas do pdf
    print(f"\n\nLendo página {indice}")
    texto_pagina=pagina.extract_text()  
    referencias = re.findall(padrao, texto_pagina)
    print(str(len(referencias))+" referencias encontradas")
    print("Referencias encontradas:")
    for x in referencias:
        print(x)
    
   



