def shopping_cart(*args):
    cart = {'Soup': [],
            'Pizza': [],
            'Dessert': []}
    for i in args:
        if i == 'Stop':
            break
        if i[0] == 'Soup' and i[1] not in cart['Soup'] and len(cart['Soup']) < 3:
            cart['Soup'].append(i[1])
        elif i[0] == 'Pizza' and i[1] not in cart['Pizza'] and len(cart['Pizza']) < 4:
            cart['Pizza'].append(i[1])
        elif i[0] == 'Dessert' and i[1] not in cart['Dessert'] and len(cart['Dessert']) < 2:
            cart['Dessert'].append(i[1])
    cart = {k: v for k, v in sorted(cart.items())}
    cart = {k: v for k, v in sorted(cart.items(), key=lambda x: len(x[1]), reverse=True)}
    res = ''
    if len(cart['Pizza']) == 0 and len(cart['Soup']) == 0 and len(cart['Dessert']) == 0:
        res = 'No products in the cart!'
    else:
        for k, v in cart.items():
            res += k + ':\n'
            for i in sorted(v):
                res += f' - {i}\n'
    return res
