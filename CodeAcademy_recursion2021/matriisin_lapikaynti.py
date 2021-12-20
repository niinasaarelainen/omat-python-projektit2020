

# negatiivisia ei lasketa
def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        if head < 0:
            head = 0
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


def matr_sum_recursive(input_matr):
    total_sum = 0
    for lista in input_matr:
        rivin_summa = list_sum_recursive(lista)
        total_sum += rivin_summa
    return total_sum



print(matr_sum_recursive([[4, 3, 2, -1, 0], [9]]))  # 18
print(matr_sum_recursive([[3, 2, -1, 0, 1, -1], [2,2,2]]))  #12