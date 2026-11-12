

def mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError('The length of y_true and y_pred should be equal')
    if len(y_true) == 0:
        raise ValueError('The length of y_true and y_pred should be greater than 0')
    total=0
    for y, y2 in zip(y_true, y_pred):
        item = abs(y-y2)**2
        total += item
    total /= len(y_true)
    return total

