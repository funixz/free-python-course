def greatest_parameter(a, b, c, d, e):
    listvars = [a, b, c, d, e]
    listvars.sort()
    return listvars[4]
    
all = greatest_parameter(1,3,5,8,9)
print (all)
