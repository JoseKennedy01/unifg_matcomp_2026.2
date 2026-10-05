'''
Parte 1: Exercícios Teóricos de Teoria dos Conjuntos
1. Seja o universo U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} e os conjuntos A = {x | x é par} e B = {x | x é primo}. 
Calcule: (a) A ∪ B; (b) A ∩ B; (c) A - B; (d) (A ∪ B)'.
2. Utilizando as Leis de De Morgan e as propriedades distributivas, simplifique a expressão de conjuntos: (A ∩ B) ∪ (A ∩ B').
3. Explique detalhadamente como o interpretador CPython trata colisões de hash na estrutura `set` e por que a busca é O(1) médio.
'''

# 1º - Operações com conjuntos:
# U = universo, A = nums pares e B = nums primos.

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {2, 4, 6, 8, 10}
B = {2, 3, 5, 7}

# a) União: elementos que pertencem a A ou a B:
uniao = A | B

# b) Interseção: elementos que pertencem a A e a B:
intersecao = A & B

# c) Diferença: elementos de A que nao pertencem a B:
diferenca = A - B

# d) Complemento da união em relação ao universo U:
complemento_da_uniao = U - uniao

# 2º - Simplificando a expressão (A ∩ B) ∪ (A ∩ B'):

# Complemento de B em relação ao universo U:
complemento_b = U - B

# Expressão original do enunciado:
expressao_original = (A & B) | (A & complemento_b)

# Pela propriedade distributiva:
# (A & B) | (A & B') = A & (B | B'), colocando em evidência.
passo_distributivo = A & (B | complemento_b)

# Como B | B' = U e A & U = A, o resultado final é A.
simplificacao = A

# Confirma que os tres resultados representam o mesmo conjunto.
assert expressao_original == passo_distributivo == simplificacao

# 3º - Explicando como o CPython trata colisões de hash na estrutura set e porque busca o O(1) médio:

'''
- CPython usa endereçamento aberto em seus sets.
- Em uma colisão, ele busca outra posição na mesma tabela, sem criar listas externas para guardar os elementos.
- A busca inicia em um índice calculado a partir do hash.
- Depois, o CPython verifica algumas posições proximas e, se necessário, usa uma sequência de sondagem baseada no hash.
- A tabela é redimensionada antes de ficar muito ocupada.
- Por isso, em média, operações como "elemento in conjunto" possuem complexidade O(1).
- No pior caso teórico, muitas colisões podem causar O(n).
'''

# Exibicao dos resultados.
print("U =", sorted(U))
print("A =", sorted(A))
print("B =", sorted(B))
print()

print("A uniao B =", sorted(uniao))
print("A intersecao B =", sorted(intersecao))
print("A diferenca B =", sorted(diferenca))
print("Complemento de A uniao B =", sorted(complemento_da_uniao))
print()

print("Expressao original =", sorted(expressao_original))
print("Passo distributivo =", sorted(passo_distributivo))
print("Simplificacao final =", sorted(simplificacao))
