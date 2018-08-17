# O volume atual de um reservatório de água (em metros cúbicos)
reservoir_volume = 4.445e8
# A quantidade de precipitação de uma tempestade (em metros cúbicos)
rainfall = 5e6

# diminuir a variável rainfall em 10% para contabilizar o escoamento
rainfall *= .9

# adicionar o valor da variável rainfall na variável reservoir_volume
reservoir_volume += rainfall

# aumentar a variável reservoir_volume em 5% para contabilizar a água da chuva que flui
# para reservatório nos dias seguintes à tempestade
reservoir_volume *= 1.05

# diminuir a variável reservoir_volume em 5% para contabilizar a evaporação
reservoir_volume *= 0.95

# subtrair 2.5e5 metros cúbicos de reservoir_volume para considerar a água
# que é canalizada para regiões áridas.
reservoir_volume -= 2.5e5 

# exibir o novo valor da variável reservoir_volume
print(reservoir_volume)