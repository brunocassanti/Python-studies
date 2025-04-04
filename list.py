class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Caixa:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, nome, preco):
        produto = Produto(nome, preco)
        self.__produtos.append(produto)
        print(f"Produto '{nome}' adicionado por R${preco:.2f}.")

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.nome == nome:
                self.__produtos.remove(produto)
                print(f"Produto '{nome}' removido.")
                return
        print(f"Produto '{nome}' não encontrado.")

    def mostrar_produtos(self):
        if not self.__produtos:
            print("Nenhum produto adicionado.")
        else:
            print("Produtos na compra:")
            for produto in self.__produtos:
                print(f"- {produto.nome}: R${produto.preco:.2f}")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.__produtos)
        return total

    def finalizar_compra(self):
        total = self.calcular_total()
        print(f"Total da compra: R${total:.2f}")
        self.__produtos = [] 
        print("Compra finalizada. Volte sempre, obrigado!")