class Produto:
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.Produto = {}

    def adicionar_produto(self,Produto):
        if Produto.nome not in self.Produto:
            self.Produto[Produto.nome] = Produto.quantidade
        else:
            self.Produto[Produto.nome] += Produto.quantidade

    def verifica_quantidade(self,nome_produto):
        return self.Produto.get(nome_produto,0)