""" Em um software monitor, que verifica a resiliência de outro software,
 precisamos saber qual o tempo máximo que um software permaneceu sem
  instabilidades. Para isto, a cada hora é feito uma requisição ao sistema
   e verificamos se está ok. Supondo um array que contenha os estados coletados
    por nosso software, calcule quanto tempo máximo que o servidor permaneceu
     sem instabilidades. """

# 1 - OK
# 2 - Instabilidade

valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]  # resultado = 3
valores_coletados2 = [1, 1, 1, 1, 0, 0, 1, 1]  # resultado = 4


def max_stability(values):
    appear = 1
    sequences = []
    for index in range(len(values) - 1):
        # print((len(values)))
        if values[index] == values[index + 1]:
            appear += 1

        if values[index] != values[index + 1]:
            sequences.append(appear)
            appear = 1

    sequences.append(appear)
    return max(sequences)


print(max_stability(valores_coletados))
print(max_stability(valores_coletados2))
