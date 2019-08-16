from projetoConclusao.Animal import Animal

#ATUALIZA TABELA
animal = Animal()
animal.restartaTabela()

#INSERE DADOS
dadosAnimal = {'nome': 'Cavalo', 'tipo': 'mamifero', 'mediaVida': 30}
animal.insereDados(dadosAnimal)
dadosAnimal = {'nome': 'Cachorro', 'tipo': 'mamifero', 'mediaVida': 17}
animal.insereDados(dadosAnimal)
dadosAnimal = {'nome': 'Cavalo', 'tipo': 'mamifero', 'mediaVida': 25}
animal.insereDados(dadosAnimal)

#ATUALIZA DADOS
dadosAtualizar = {'campo': 'nome', "valor": "'Elefante'", "condicional": "media_vida = 25"}
animal.autalizaDados(dadosAtualizar)

#DELETA DADOS
dadosDeletar = {'campo': 'media_vida', 'valor': 30}
animal.deletaDados(dadosDeletar)

#SELECIONA DADOS
dadosSelecionar = {'campos': '*'}
dadosRetornados = animal.selecionaDados(dadosSelecionar)
print("Animais retornados da tabela: \n ", dadosRetornados)