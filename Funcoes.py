def perguntar():
    return input("O que deseja realizar: \n" +
                 "< I > - Inserir um usuário\n" +
                 "< P > - Pesquisar um usuário\n" +
                 "< E > - Excluir um usuário\n" +
                 "< L > - Listar um usuário\n").upper()
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                         input("Digite a data de acesso: "),
                                                         input("Qual a estação: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("db.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))