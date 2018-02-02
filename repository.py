import dataset

from database import conexao

class ProdutoRepository:
    def add(self, produto):
        return conexao.insert(produto)
    def alter(self, produto):
        return conexao.alter(produto)
