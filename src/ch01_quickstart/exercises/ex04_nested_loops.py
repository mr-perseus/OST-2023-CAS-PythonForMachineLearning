def print_number_triangle(number_of_rows):
    for current_row_index in range(1, number_of_rows + 2):
        for current_column_index in range(1, current_row_index):
            print(str(current_column_index), end='')
        print()

print_number_triangle(3)
print_number_triangle(4)


def print_triangle(number_of_rows):
    index = 1

    for current_row_index in range(1, number_of_rows + 2):
        for current_column_index in range(1, current_row_index):
            print(str(index), end=' ')
            index += 1
        print()


print_triangle(4)