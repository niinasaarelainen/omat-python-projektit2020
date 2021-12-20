def list_sum_recursive(input_list):
    if input_list == []:
        return 0

    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        print(head , smaller_list)
        return head + list_sum_recursive(smaller_list)


print(list_sum_recursive([4, 3, 2]))