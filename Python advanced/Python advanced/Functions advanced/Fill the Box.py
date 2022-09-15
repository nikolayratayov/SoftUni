def fill_the_box(*args):
    space = args[0] * args[1] * args[2]
    stop = False
    cubes = 0
    for i in range(3, len(args)):
        if args[i] == 'Finish':
            break
        if not stop:
            space -= args[i]
            if space <= 0:
                stop = True
                cubes += abs(space)
        else:
            cubes += args[i]
    if not stop:
        return f'There is free space in the box. You could put {space} more cubes.'
    else:
        return f'No more free space! You have {cubes} more cubes.'
