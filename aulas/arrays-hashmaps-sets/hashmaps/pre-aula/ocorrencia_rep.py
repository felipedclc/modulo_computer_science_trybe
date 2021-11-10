# quais elementos da lista A também ocorrem na lista B

list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]


def old_scholl(list1, list2):
    max_length = 0
    rep_list = []
    if len(list1) > len(list2):
        max_length = len(list1)
    else:
        max_length = len(list2)

    for i in range(max_length):
        for j in range(max_length):
            if list1[i] == list2[j]:
                rep_list.append(list1[i])

    return rep_list


print(old_scholl(list_a, list_b))


def most_efficient(list1, list2):
    return [num for num in list1 if num in list2]


print(most_efficient(list_a, list_b))


def intersecion(list1, list2):
    seen_in_a = {}
    for num in list1:
        if num not in seen_in_a:
            seen_in_a[num] = True

    final_list = []
    for num in list2:
        if num in seen_in_a:
            final_list.append(num)

    return seen_in_a


print(intersecion(list_a, list_b))
