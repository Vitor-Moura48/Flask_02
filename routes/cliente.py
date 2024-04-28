from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

'''
Rota de Clientes

    - /clientes/ - listar os clientes
    - /clientes/ - Inserir o cliente no servidor
    - /clientes/new - renderizar o formulário para criar um cliente
    - /clientes/<id> - obter os dados de um cliente
    - /clientes/<id>/edit - renderizar um formulário para editar um cliente
    - /cliente/<id>/update - atualizar os dados do cliente
    - clientes/<id>/delete - deleta o registro do usurário
'''

@cliente_route.route('/')
def lista_clientes():
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():

    data = request.form.to_dict()

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )
   
    return 'Cadastrado!'
    

@cliente_route.route('/new')
def form_cadastro_cliente():
    return render_template('form_cadastro_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def obter_dados_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('obter_dados_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html', cliente_id=cliente_id)

@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
def update_cliente(cliente_id):

    data = request.form.to_dict()

    cliente_atualizado = Cliente.get_by_id(cliente_id)
    cliente_atualizado.nome = data['nome']
    cliente_atualizado.email = data['email']
    cliente_atualizado.save()

    return 'Cliente Atualizado!'


@cliente_route.route('/<int:cliente_id>/delete')
def delete_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
  
    return 'Eliminado!'
   

