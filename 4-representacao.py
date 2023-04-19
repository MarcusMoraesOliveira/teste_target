faturamento_distribuidora = [ {'estado': 'SP', 'faturamento': 67836.43},
                              {'estado': 'RJ', 'faturamento': 36678.66},
                              {'estado': 'MG', 'faturamento': 29229.88},
                              {'estado': 'ES', 'faturamento': 27165.48},
                              {'estado': 'Outros', 'faturamento': 19849.53}]

total_mensal = 0.0

for dados in faturamento_distribuidora:
    total_mensal += dados['faturamento']

for dados in faturamento_distribuidora:
    dados['percentual'] = (dados['faturamento'] * 100) / total_mensal

print(faturamento_distribuidora)

for dados in faturamento_distribuidora:
    print(str(dados['estado']) + ": " + str(dados['percentual']))
