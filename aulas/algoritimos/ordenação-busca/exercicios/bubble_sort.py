from Cronometro import Cronometro


input = ["zebra", "macaco", "elefante", "arara", "javali"]

with Cronometro("Algoritmo"):

    def bubble_sort(array):
        # Quando falsa, indica que o array está ordenado
        has_swapped = True

        # armazena o número de iterações para evitar indices já ordenados
        num_of_iterations = 0

        # Enquanto ainda não está ordenado (ocorreram trocas na iteração)
        while has_swapped:
            has_swapped = False

            # percorra o array até o ultimo índice não ordenado
            for index in range(len(array) - num_of_iterations - 1):
                # caso a posição corrente seja maior que a posterior
                if array[index] > array[index + 1]:
                    # marca que tivemos trocas nesta iteração
                    has_swapped = True
            num_of_iterations += 1

        return array
