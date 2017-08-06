def check_if_none(a, b, c, d, e):
    list=[str(a),str(b),str(c),str(d),str(e)]
    if 'None' in list:
        return True;
    else:
        return False;

check_if_none('None', 2, 3, 4, 5)
