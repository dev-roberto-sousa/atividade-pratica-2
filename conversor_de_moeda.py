"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_em_reais = 100
taxa_do_dolar = 5.20
tava_do_euro = 6.15

valor_convertido_dolar = valor_em_reais / taxa_do_dolar
valor_convertido_euro = valor_em_reais / tava_do_euro

print(f"O valor convertido para Dolares é: ${valor_convertido_dolar:.2f}")
print(f"O valor convertido para Euros é: €{valor_convertido_euro:.2f}")
