import dataset

from database import produtos, tipos

class ProdutoRepository:
    def add(self, produto):
        return produtos.insert(produto)
    def alter(self, produto):
        return produtos.alter(produto)
    def add_tipo(self, tipo):
        return tipos.insert(tipo)
    
    
