#importando bibliotecas
import PyPDF2
import os

# criando ferramenta para mesclar
merger = PyPDF2.PdfMerger()

#listando e ordenando arquivos
caminho = "C:/Users/Desktop/PORTFOLIO_PYTHON/ARQUIVOS"
lista_arquivos = os.listdir(caminho)
lista_arquivos.sort()
print(lista_arquivos)

#juntando pdfs através de condicionais, pra cada arquivo no formato .pdf, adicione ao arquivo final
for arquivo in lista_arquivos:
    if arquivo.lower().endswith(".pdf"):
        merger.append(f"{caminho}/{arquivo}")


#salvar pdf final
merger.write("RA_Geral")