def stock_availability(boxes, *args):
    if args[0] == 'delivery':
        for i in range(1, len(args)):
            boxes.append(args[i])
    else:
        if len(args) == 1:
            boxes.pop(0)
        else:
            try:
                for i in range(int(args[1])):
                    boxes.pop(0)
            except:
                for i in range(1, len(args)):
                    while True:
                        if len(boxes) == 0:
                            break
                        if args[i] not in boxes:
                            break
                        boxes.remove(args[i])
    return boxes
