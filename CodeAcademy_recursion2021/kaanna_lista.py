def kaanna_lista2(lista, new_list):
    if lista == []:
        return    # huom !!! sama kuin return 0
    
    new_list.append(lista.pop(-1))
    kaanna_lista(lista, new_list)
    return new_list



def kaanna_lista(input_list, new_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        tail = input_list[-1]
        smaller_list = input_list[:-1]
        new_list.append(tail)
        kaanna_lista(smaller_list, new_list)
        return new_list


print(kaanna_lista([4, 3, 2], []))
print(kaanna_lista([2, 4, 6, 8, 10], []))

print(kaanna_lista2([4, 3, 2], []))
print(kaanna_lista2([2, 4, 6, 8, 10], []))