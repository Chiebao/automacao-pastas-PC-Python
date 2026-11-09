import os
from tkinter.filedialog import askdirectory

# Janela para escolher a pasta que vai ser organizada
caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

# Regras de organização: nome da subpasta -> extensões que vão para ela
locais = {
    'imagens': ['.png', '.jpg', '.jpeg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    extensao = extensao.lower()  # trata .PNG e .png do mesmo jeito
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
