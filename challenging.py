def maximum_num( x, y, z ):
    if x > y and y < z:
        return x
    if y > z and z < x:
        return y
    else:
        return z
    return ( x, y, z ) 
print(maximum_num(7,9,5))