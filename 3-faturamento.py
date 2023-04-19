import json
  
f = open('dados.json')
  
data = json.load(f)

menor_faturamento = 100000000.0
maior_faturamento = 0.0
media = 0.0
valores_media = 0

for dados in data:
    if dados['valor'] != 0.0:
        media += dados['valor']
        valores_media = valores_media + 1
        if dados['valor'] > maior_faturamento:
            maior_faturamento = dados['valor']
        if dados['valor'] < menor_faturamento:
            menor_faturamento = dados['valor']

media = media / valores_media

dias_maior_media = 0

for dados in data:
    if dados['valor'] > media:
        dias_maior_media = dias_maior_media + 1

print("O menor valor de faturamento ocorrido foi " + str(menor_faturamento))
print("O maior valor de faturamento ocorrido foi " + str(maior_faturamento))
print("O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi " + str(dias_maior_media) + " dias")


        
