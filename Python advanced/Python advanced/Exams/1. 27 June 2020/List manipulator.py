def list_manipulator(nums, *args):
    if args[0] == 'add':
        if args[1] == 'beginning':
            for i in range(len(args) - 1, 1, -1):
                nums.insert(0, i)
        else:
            for i in range(2, len(args)):
                nums.append(i)
    else:
        if args[1] == 'beginning':
            if len(args) == 2:
                nums.pop(0)
            else:
                for i in range(args[2]):
                    nums.pop(0)
        else:
            if len(args) == 2:
                nums.pop()
            else:
                for i in range(args[2]):
                    nums.pop()
    return nums
