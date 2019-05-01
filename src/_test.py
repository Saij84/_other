x = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]

if __name__ == '__main__':
    arr = []

    data_in = [[i] for i in x.split("\n") if not i == ""]
    print(data_in)

    for i in data_in:
        for num in i:
            arr_str = ("".join([x for x in num if not x == " "]))
            arr.append([int(a) for a in arr_str])
    print(arr)