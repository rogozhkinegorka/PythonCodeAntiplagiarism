import ast


def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def preprocess(code):
    tree = ast.parse(code)

    # To do function annotations remove
    # To do functions and variables name change

    return ast.unparse(tree)


def compare(code_1, code_2):
    code_1 = preprocess(code_1)
    code_2 = preprocess(code_2)
    return levenstein(code_1, code_2) * 2 / (len(code_1) + len(code_2))


def compare_all(input_file, output_file):
    o_f = open(output_file, "w")
    i_f = open(input_file, 'r')
    for row in i_f:
        file_1, file_2 = row.split
        with open(file_1) as f1:
            code_1 = f1.read()
        with open(file_2) as f2:
            code_2 = f2.read()

        diff = compare(code_1, code_2)
        o_f.write(str(diff))

    i_f.close()
    o_f.close()


input_file, output_file = input().split()
compare_all(input_file, output_file)

