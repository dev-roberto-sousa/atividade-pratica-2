"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_do_produto = "Camiseta"

preco_original = 50.00
porcentagem_desconto = 20 / 100
valor_desconto = preco_original * porcentagem_desconto
preco_final = preco_original - valor_desconto

print(
    f"Nome do Produto: {nome_do_produto}\n"
    f"Preço original: R${preco_original:.2f}\n"
    f"Porcentagem de desconto: {porcentagem_desconto:.0%}\n"
    f"Valor do desconto: R${valor_desconto:.2f}\n"
    f"Valor final: R${preco_final:.2f}"
    )
