import PyPDF2


#Inicialização do PDF e contador de páginas
arquivo_path="ementa_computacao_bac.pdf" #Se quiser testar com outro pdf é só mudar esse valor do nome
arquivo_aberto = PyPDF2.PdfReader(arquivo_path) 
print(f"{len((arquivo_aberto.pages))} Páginas encontradas")


#Define os termos comuns encontrados nas páginas individuais de disciplinas
#Nessa parte que dá pra implementar Regex
termos_comuns=["DISCIPLINA","CRÉDITOS","BIBLIOGRAFIA","ED.","BIBLIOGRAFIA COMPLEMENTAR","BIBLIOGRAFIA BÁSICA"]

#Importante: Adaptado pra pdfs que possuem uma página por matéria!

for indice,pagina in enumerate(arquivo_aberto.pages): #Percorre as páginas do pdf
    print(f"Lendo página {indice}")
    termos_encontrados=0                  #Contar quantos termos comuns tem na página
    texto_pagina=pagina.extract_text()
    for termo in termos_comuns:
        if termo.upper() in texto_pagina:
            termos_encontrados+=1
    if termos_encontrados>=3:       #Resultado da contagem de termos
        print("  >Possivel pagina de disciplina, adicionar para merge\n")
    else: 
        print("  >Possivelmente não é página de disciplina, descartar\n")