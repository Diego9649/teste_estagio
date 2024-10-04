import json

# Exemplo de dados de faturamento em formato JSON
faturamento = """
{
    "dias": [
        {"dia": 1, "valor": 1500},
        {"dia": 2, "valor": 3000},
        {"dia": 3, "valor": 0},
        {"dia": 4, "valor": 500},
        {"dia": 5, "valor": 0},
        {"dia": 6, "valor": 800}
    ]
}
"""

dados = json.loads(faturamento)

valores = [dia['valor'] for dia in dados['dias'] if dia['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
