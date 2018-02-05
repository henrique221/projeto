import dataset

from database import db, produtos, tipos

class ProdutoRepository:
    def add(self, produto):
        return produtos.insert(produto)
    def alter(self, produto):
        return produtos.alter(produto)
    def add_tipo(self, tipo):
        return tipos.insert(tipo)
    def join_produto_tipo(self):
        return db.query('select * from produtos inner join tipos_produtos on tipos_produtos.id = produtos.tipo')
