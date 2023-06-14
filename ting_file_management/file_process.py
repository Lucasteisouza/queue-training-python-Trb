from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    text = txt_importer(path_file)

    for entry in range(0, len(instance)):
        if instance.search(entry)["nome_do_arquivo"] == path_file:
            return None

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }
    instance.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")
        return None
    current_file = instance.peek()
    current_file_name = current_file["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {current_file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        instance.search(position)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
        return None
    print(instance.search(position))
