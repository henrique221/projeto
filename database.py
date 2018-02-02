import dataset

db = dataset.connect('sqlite:///produtos.db')
conexao = db['produtos']
