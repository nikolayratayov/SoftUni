import copy

substrings = input().split(' ')
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
colors = []
while True:
    if len(substrings) == 0:
        break
    if len(substrings) == 1:
        try_color = substrings.pop()
        if try_color in main_colors or try_color in secondary_colors:
            colors.append(try_color)
        else:
            try_color = try_color[:len(try_color) - 1]
            if len(try_color) == 0:
                break
    else:
        first = substrings.pop(0)
        second = substrings.pop()
        try_color = first + second
        try_color_sec = second + first
        if try_color in main_colors or try_color in secondary_colors:
            colors.append(try_color)
        elif try_color_sec in main_colors or try_color_sec in secondary_colors:
            colors.append(try_color_sec)
        else:
            first = first[:len(first) - 1]
            second = second[:len(second) - 1]
            first_idx = len(substrings) // 2
            second_idx = len(substrings) // 2 + 1
            if len(first) == 0 and len(second) != 0:
                substrings.insert(first_idx, second)
            elif len(second) == 0 and len(first) != 0:
                substrings.insert(first_idx, first)
            elif len(first) != 0 and len(second) != 0:
                substrings.insert(first_idx, first)
                substrings.insert(second_idx, second)

copy_of_colors = copy.copy(colors)
for i in copy_of_colors:
    if i == 'orange':
        if 'red' not in colors or 'yellow' not in colors:
            colors.remove(i)
    elif i == 'purple':
        if 'red' not in colors or 'blue' not in colors:
            colors.remove(i)
    elif i == 'green':
        if 'yellow' not in colors or 'blue' not in colors:
            colors.remove(i)
print(colors)
