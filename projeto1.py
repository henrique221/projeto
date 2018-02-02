# coding: utf-8

from database import conexao
from repository import ProdutoRepository
from flask import Flask, request, url_for, current_app, send_from_directory, render_template, redirect
import os

app = Flask(__name__, static_folder='assets')



@app.route("/", methods=["GET", "POST"])

def cadastrar():
    repository = ProdutoRepository(),
    todos_os_produtos = list(conexao.all())
    if request.method == "POST":

        dados_do_form = request.form.to_dict() 
        dados_do_form['preco'] = int(dados_do_form['preco'])         

        repository = ProdutoRepository()

        nome_novo_produto = repository.add(dados_do_form)
        return render_template(
            'cadastrook.html',
            nome_novo_produto = dados_do_form['nome']
        )

    return render_template(
        'index.html',
        title=u"Inserir novo produto",   
        todos_os_produtos = todos_os_produtos       
        
    )
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)