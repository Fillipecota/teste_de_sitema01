def cadastro(nome, idade, telefone, email):
    if " " in nome and "48" in telefone and "@" in email:
        return True
    else:
        return "dados invalidos:  verificar  nome , telefone ou email."

    