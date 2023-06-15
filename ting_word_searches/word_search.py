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
    existing_word_list = exists_word(word, instance)
    if len(existing_word_list) > 0:
        for i in range(0, len(existing_word_list)):
            occorrencias_atual = existing_word_list[i]["ocorrencias"]
            for j in range(0, len(occorrencias_atual)):
                linha_atual = occorrencias_atual[j]["linha"]
                text_atual = instance.search(i)["linhas_do_arquivo"]
                occorrencias_atual[j]["conteudo"] = text_atual[linha_atual - 1]
    return existing_word_list
