def exists_word(word, instance):
    output_list = []
    for i in range(0, len(instance)):
        search_result = instance.search(i)
        entry_ocurrances = {
            "palavra": word,
            "arquivo": search_result["nome_do_arquivo"],
            "ocorrencias": []
        }
        for j in range(0, len(search_result["linhas_do_arquivo"])):
            if word.lower() in search_result["linhas_do_arquivo"][j].lower():
                entry_ocurrances["ocorrencias"].append({"linha": j + 1})
        if len(entry_ocurrances["ocorrencias"]) > 0:
            output_list.append(entry_ocurrances)
    return output_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
