def bubble_sort(my_list):
    last_index = len(my_list) - 1
    for i in range(0, last_index):
        for j in range(0, last_index - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


if __name__ == '__main__':
    example_list = [4,1,8,7,10,9,3,2,5,6]
    print(bubble_sort(example_list))
