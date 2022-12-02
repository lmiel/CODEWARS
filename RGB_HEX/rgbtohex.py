def rgb(r,g,b): #la funcion acepta como entrada red, blue y green
    ret = ""
    if r<16:#si es menor que 10 hay q meter un 0
        ret += "0"
    if r<0:
        ret += "0"
    elif r<256:#si es mayor que 16 hay que escribir 00
        ret += str(hex(r)).upper()[2:4] #la funcion hex tranforma el numero en hexadecimal
    else:
        ret+= "FF"
    if g<16:
        ret += "0"
    if g<0:
        ret += "0"
    elif g<256:
        ret += str(hex(g)).upper()[2:4]
    else:
        ret+= "FF"
    if b<16:
        ret += "0"
    if b<0:
        ret += "0"
    elif b<256:
        ret += str(hex(b)).upper()[2:4]
    else:
        ret+= "FF"
    return ret
print(rgb(-5,-99,116))
