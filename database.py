import dataset

db = dataset.connect('sqlite:///produtos.db')
produtos = db['produtos']
tipos = db['tipos_produtos']
