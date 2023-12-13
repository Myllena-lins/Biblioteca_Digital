import json
from functools import reduce
import csv
import statistics

# Ler uma lista de objetos de um JSON
with open("books.json", "r") as arq:
    lista_livros = json.load(arq)

# Obter uma lista com os nomes dos livros
print("Nomes dos livros:\n", list(map(lambda l: l["nome"], lista_livros)))

# Realizar um mapeamento, um filtro e uma redução (utilizar lambda function)
livros_estoque = list(filter(lambda l: l["estoque"], lista_livros))
print("Existem no estoque:\n", list(map(lambda l: l["nome"], livros_estoque)))

total_livros = len(lista_livros)
preco_medio = reduce(lambda soma, l: soma +
                     l["preco"], lista_livros, 0) / total_livros
print(f"O preço médio dos livros é: {preco_medio:.2f}")

# Permitir que os dados possam ser aumentados, listados, lidos individualmente, atualizados e excluídos (manter JSON atualizado)
# Garantir que todas as operações tenham validações (try-except, raise)
# Listar os livros


def mostra_todos_livros(lista_livros):
    print("Segue a lista de todos os livros:")
    for livro in lista_livros:
        print("-----------------------------")
        print("Nome:", livro["nome"])
        print("Autor:", livro["autor"])
        print("Quantidade de páginas:", livro["quantidade_pagina"])
        print("Quantidade disponível:", livro["quantidade_disponivel"])
        print("Preço:", livro["preco"])
        print("Em estoque:", livro["estoque"])
        print("-----------------------------")


mostra_todos_livros(lista_livros)

# Adicionar um novo livro


def atualiza_JSON(lista_livros):
    with open("books.json", "w") as arq:
        arq.write(json.dumps(lista_livros, indent=2))


def adicionar_livro(lista_livros, livro):
    try:
        if not isinstance(livro, dict):
            raise ValueError("O livro deve ser um dicionário.")
        # Adicionar validações adicionais conforme necessário
        lista_livros.append(livro)
        atualiza_JSON(lista_livros)
        print("Livro adicionado com sucesso.")
    except ValueError as e:
        print(f"Erro ao adicionar livro: {e}")


# Remover os dados redundantes "Todo caminho diante de mim"
livro_repetido = {
    "nome": "Todo caminho diante de mim",
    "autor": "C.S. Lewis",
    "quantidade_pagina": 288,
    "quantidade_disponivel": 15,
    "preco": 59.9,
    "estoque": True,
}
lista_livros = [livro for livro in lista_livros if livro != livro_repetido]

# Visualizar um livro


def visualizar_livro(lista_livros, indice):
    try:
        livro = lista_livros[indice]
        print("-----------------------------")
        print("Nome:", livro["nome"])
        print("Autor:", livro["autor"])
        print("Quantidade de páginas:", livro["quantidade_pagina"])
        print("Quantidade disponível:", livro["quantidade_disponivel"])
        print("Preço:", livro["preco"])
        print("Em estoque:", livro["estoque"])
        print("-----------------------------")
    except IndexError:
        print("Índice fora do alcance. O livro não pode ser visualizado.")


print("Seguem as informações referentes ao quinto livro:\n")
visualizar_livro(lista_livros, 8)

# Atualizar um livro


def atualizar_livro(lista_livros, indice, dados_livro):
    try:
        if not isinstance(dados_livro, dict):
            raise ValueError("Os dados do livro devem ser um dicionário.")
        # Adicionar validações adicionais conforme necessário
        lista_livros[indice] = dados_livro
        atualiza_JSON(lista_livros)
        print("Livro atualizado com sucesso.")
        return lista_livros[indice]
    except IndexError:
        print("Índice fora do alcance. O livro não pode ser atualizado.")
    except ValueError as e:
        print(f"Erro ao atualizar livro: {e}")


livro_atualizada = {
    "nome": "O problema do sofrimento",
    "autor": "C.S. Lewis",
    "quantidade_pagina": 160,
    "quantidade_disponivel": 100,
    "preco": 39.90,
    "estoque": True,
}
print("O livro atualizado foi:", atualizar_livro(
    lista_livros, 2, livro_atualizada))

# Remover um livro


def remover_livro(lista_livros, indice):
    try:
        livro = lista_livros.pop(indice)
        atualiza_JSON(lista_livros)
        print("Livro removido com sucesso.")
        return livro
    except IndexError:
        print("Índice fora do alcance. O livro não pode ser removido.")


print("O livro removido foi:", remover_livro(lista_livros, 7))

# Mínimo e máximo


def get_min_max_by_attribute(lista, attribute, get_min=True):
    try:
        if not lista or not isinstance(lista, list):
            raise ValueError("A lista é inválida.")

        if not lista[0].get(attribute):
            raise ValueError(
                f"O atributo '{attribute}' não existe nos elementos da lista.")

        min_max_value = lista[0][attribute]
        result = [(lista[0]["nome"], min_max_value)]

        for elemento in lista[1:]:
            valor_atual = elemento.get(attribute)

            if valor_atual is None:
                raise ValueError(
                    f"O atributo '{attribute}' não existe em alguns elementos da lista.")

            if get_min and valor_atual < min_max_value:
                min_max_value = valor_atual
                result = [(elemento["nome"], valor_atual)]
            elif not get_min and valor_atual > min_max_value:
                min_max_value = valor_atual
                result = [(elemento["nome"], valor_atual)]
            elif valor_atual == min_max_value:
                result.append((elemento["nome"], valor_atual))

        return result

    except ValueError as e:
        return f"Erro ao obter valor máximo/mínimo: {e}"


max_paginas = get_min_max_by_attribute(
    lista_livros, "quantidade_pagina", get_min=False)
print("O máximo de página é:", max_paginas)

min_paginas = get_min_max_by_attribute(
    lista_livros, "quantidade_pagina", get_min=True)
print("O mínimo de página é:", min_paginas)

max_preco = get_min_max_by_attribute(lista_livros, "preco", get_min=False)
print("O preço máximo é:", max_preco)

min_preco = get_min_max_by_attribute(lista_livros, "preco", get_min=True)
print("O preço mínimo é:", min_preco)

# Dados estatísticos do preço dos livros
precos = [livro["preco"] for livro in lista_livros]

media = sum(precos) / len(precos)
print(f"Média dos preços dos livros é: {media:.2f}")

mediana = statistics.median(precos)
print(f"Mediana dos preços dos livros é: {mediana:.2f}")

moda = statistics.mode(precos)
print(f"Moda dos preços dos livros é: {moda:.2f}")

desvio_padrao = statistics.stdev(precos)
print(f"Desvio padrão dos preços dos livros é: {desvio_padrao:.2f}")

# Dados estatísticos da quantidade de livros no estoque
estoque = [livro["quantidade_disponivel"] for livro in lista_livros]

media = sum(estoque) / len(estoque)
print(f"Média da quantidade de livros no estoque é: {media:.2f}")

mediana = statistics.median(estoque)
print(f"Mediana da quantidade de livros no estoque é: {mediana:.2f}")

moda = statistics.mode(estoque)
print(f"Moda da quantidade de livros no estoque é: {moda:.2f}")

desvio_padrao = statistics.stdev(estoque)
print(
    f"Desvio padrão da quantidade de livros no estoque é: {desvio_padrao:.2f}")

# Dados estatísticos da quantidade de páginas dos livros
paginas = [livro["quantidade_pagina"] for livro in lista_livros]

media = sum(paginas) / len(paginas)
print(f"Média da quantidade de páginas dos livros é: {media:.2f}")

mediana = statistics.median(paginas)
print(f"Mediana da quantidade de páginas dos livros é: {mediana:.2f}")

moda = statistics.mode(paginas)
print(f"Moda da quantidade de páginas dos livros é: {moda:.2f}")

desvio_padrao = statistics.stdev(paginas)
print(
    f"Desvio padrão da quantidade de páginas dos livros é: {desvio_padrao:.2f}")

# Salvar dados estatísticos em um arquivo CSV
dados_estatisticos = [media, mediana, moda, desvio_padrao]

with open("estatisticas.csv", "w", newline='') as arq:
    writer = csv.writer(arq)
    writer.writerow(["Média", "Mediana", "Moda", "Desvio padrão"])
    writer.writerow(dados_estatisticos)

# Ler dados estatísticos de um arquivo CSV e converter para um dicionário
with open("estatisticas.csv", "r", newline='') as arq:
    reader = csv.DictReader(arq)
    for linha in reader:
        print(linha["Média"], linha["Mediana"],
              linha["Moda"], linha["Desvio padrão"])