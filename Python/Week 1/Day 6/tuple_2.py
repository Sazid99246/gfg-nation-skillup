def sequence(tup):
    a = list(tup)
    sequence_variance = tup[1] - tup[0]
    for i in range(3):
        next_element = a[-1] + sequence_variance
        a.append(next_element)
    
    return tuple(a)
