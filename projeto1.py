# coding: utf-8

from database import produtos, tipos
from repository import ProdutoRepository
from flask import Flask, request, url_for, current_app, send_from_directory, render_template, redirect
import os

app = Flask(__name__, static_folder='assets')

@app.route("/", methods=["GET", "POST"])

def cadastrar_produto():
    repository = ProdutoRepository()
    if request.method == "POST":

        dados_do_form = request.form.to_dict() 
        dados_do_form['preco'] = float(dados_do_form['preco'])         

        nome_novo_produto = repository.add(dados_do_form)
        return render_template(
            'cadastrook.html',
            nome_novo_produto = dados_do_form['nome']
        )


    return render_template(
        'index.html',
        title=u"Inserir novo produto",   
        lista_produtos = repository.join_produto_tipo(),
        tipos = list(tipos.all())
    )

@app.route("/tipo", methods=['GET', 'POST'])

def cadastrar_tipo():
    repository = ProdutoRepository()
    
    if request.method == "POST":
        form = request.form.to_dict()
        novo_tipo = repository.add_tipo(form)
        return render_template(
            'tipo_ok.html',
            novo_tipo = form['tipo']
        )
    return render_template(
        'tipo.html',
        title=u"Inserir novo tipo",
        lista_tipos = list(tipos.all())
    )
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)