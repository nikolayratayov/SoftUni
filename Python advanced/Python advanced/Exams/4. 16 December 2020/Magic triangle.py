def get_magic_triangle(n):
    magic_triangle = [[1]]
    for i in range(n - 1):
        new_list = []
        for j in range(len(magic_triangle[i]) + 1):
            first = 0
            try:
                if j - 1 < 0:
                    raise Exception
                first += magic_triangle[i][j - 1]
            except:
                pass
            second = 0
            try:
                second += magic_triangle[i][j]
            except:
                pass
            new_list.append(first + second)
        magic_triangle.append(new_list)
    return magic_triangle
