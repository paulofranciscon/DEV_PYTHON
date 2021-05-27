with open("first_file.txt", "r") as arquivo:
    """
    ## Nesta forma lê o aquivo inteiro
    conteudo = arquivo.read()
    """
    ### Nesta forma lê a primeira linha
    conteudo = arquivo.readline()

    for linha in arquivo.readlines():
        print(linha)