def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'
    products = {}
    for k, v in kwargs.items():
        if len(products) == 5:
            break
        if v[0] * v[1] <= budget:
            if k not in products:
                products[k] = v[0] * v[1]
            else:
                products[k] += v[0] * v[1]
            budget -= v[0] * v[1]
    res = ''
    for k, v in products.items():
        res += f'You bought {k} for {v:.2f} leva.\n'
    return res
