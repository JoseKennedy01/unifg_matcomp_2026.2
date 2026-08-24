# Autoria de Sensores

alpha = {'SEN-01', 'SEN-02', 'SEN-03','SEN-05', 'SEN-08', 'SEN-01'}
beta = {'SEN-03', 'SEN-04', 'SEN-05', 'SEN-06','SEN-09', 'SEN-04'}

print('')

# 1- Deduplicar via set()
alpha = set(alpha)
beta = set(beta)

print(f'1º')
print(alpha)
print(beta)

print('')

# 2- Calcular total de sensores únicos (A ∪ B)
uniao = alpha | beta # OU uniao = alpha.union(beta)
print(f'2º \n{uniao}')

print('')

# 3- Identificar sensores redundantes (A ∩ B)
intersecao = alpha & beta # OU intersecao = alpha.intersection(beta)
print(f'3º \n {intersecao}')

print('')

# 4- Identificar exclusivos da Malha Norte (A \ B)
apenas_alpha = alpha - beta # OU exclusivos_alpha = alpha.difference(beta)
print(f'4º \n{apenas_alpha}')

print('')

# 5- Identificar sensores sem sobreposição (A Δ B)
sem_sobrepos = alpha ^ beta # OU sem_sobreposicao = alpha.symmetric_difference(beta)
print(f'5º \n{sem_sobrepos}')
