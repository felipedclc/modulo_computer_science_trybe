list_a = [1, 3, 4, -43, 2, 0]
list_b = [4, 4, 9, 578, 12]

# instanciar adicionando itens
set_a_add = set()
for item in list_a:
    set_a_add.add(item)

# instanciar direto com listas
set_a_inst = set(list_a)

# instanciar com a notação de chaves (se tiver apenas chaves {1,2,3}
#  o python intende que é um set não um dict) - NÂO RECOMENDADO
set_a_not = {-3, 0, 3, 4, 40, 2, 6}


# principais operações com set
set_a = set(list_a)
set_b = set(list_b)
print(set_a.union(set_b))  # junta dois conjuntos
print(set_a.union(set_b, {-40, -50, -60, -80}))  # colocar valor em variáveis
print(set_a.intersection(set_b))  # pega o que tem em comum
print(set_a.difference(set_b))  # pega o que tem em a não tem em b
print(set_b.difference(set_a))  # pega o que tem em b não tem em a


# operadores de comparação
print(set_a == set_b)
print({1, 2, 3, 4} > {1, 2, 3})
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))
# não retorna o maior tamanho, retorna se é um subconjunto ou um superconunto,
#  usar o isSubset ou is superset
