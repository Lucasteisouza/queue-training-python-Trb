import sys


def txt_importer(path_file):
    if path_file[-4:] != '.txt':
        print("Formato inválido", file=sys.stderr)
        # raise ValueError("Formato inválido")
    try:
        with open(path_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        # raise FileNotFoundError(f"Arquivo {path_file} não encontrado")
