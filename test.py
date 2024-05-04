def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    r_new = hex(r)[-2::]
    g_new = hex(g)[-2::]
    b_new = hex(b)[-2::]
    result = str(r_new) + str(g_new) + str(b_new)
    hexa = ""
    for i in result:
        if i == "x":
            i = "0"
        hexa += i.upper()
    return hexa


print(rgb(-20, 275, 125))
