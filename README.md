# Automação para Organizar Pastas

Script em Python que organiza uma pasta bagunçada em segundos: você escolhe a pasta, e os arquivos são movidos automaticamente para subpastas de acordo com o tipo.

---

## Como funciona

1. Abre uma janela para escolher a pasta que será organizada.
2. Lê os arquivos e identifica a extensão de cada um.
3. Cria as subpastas que faltarem e move os arquivos:

| Subpasta | Extensões |
|---|---|
| `imagens` | `.png` `.jpg` `.jpeg` |
| `planilhas` | `.xlsx` |
| `pdfs` | `.pdf` |
| `csv` | `.csv` |

As regras ficam no dicionário `locais`, no início do código, e podem ser ampliadas com novas categorias e extensões.

## Como executar

```bash
python main.py
```

Não precisa instalar nada além do Python 3: o script usa apenas bibliotecas nativas (`os` e `tkinter`).

## Tecnologias

`Python` `os` `tkinter`

## Próximos passos

- Registro (log) de cada arquivo movido
- Tratamento de arquivos com o mesmo nome na pasta de destino

---

**Luana Godoy** · Estudante de Análise e Desenvolvimento de Sistemas
[LinkedIn](https://www.linkedin.com/in/luana-chiebao) · [GitHub](https://github.com/Chiebao)
