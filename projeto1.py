# coding: utf-8

from database import conexao
from repository import ProdutoRepository
from flask import Flask, request, url_for, current_app, send_from_directory, render_template, redirect

app = Flask(__name__, static_folder='assets')


@app.route("/", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":

        dados_do_form = request.form.to_dict()
        imagem = request.files.get('imagem')

          

        repository = NoticiaRespository()

        nome_novo_produto = repository.add(dados_do_form)
        return render_template(
            'cadastro_sucesso.html',
            nome_novo_produto = nome_novo_produto
        )

    return render_template(
        'index.html',
        title=u"Inserir novo produto"
    )
