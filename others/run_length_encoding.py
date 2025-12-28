def rle(input):
    if input is None or len(input) < 1:
        return ""
    
    res = []
    prev = None
    counter = 0
    for c in input:
        if c == prev or prev is None:
            counter += 1
            prev = c
        else:
            res.append(str(counter) + prev)
            counter = 1
            prev = c

    res.append(str(counter) + prev)

    return ''.join(res)


print(rle("aaabbccca"))
