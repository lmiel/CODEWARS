def rgb(r,g,b): #la funcion acepta como entrada red, blue y green
    ret = ""
    if r<10:#si es menor que 10 hay q meter un 0
        ret += "0"
    if r<255:#si es mayor que 16 hay que escribir 00
        ret += str(hex(r)).upper()[2:4] #la funcion hex tranforma el numero en hexadecimal
    else:
        ret+= "FF"
    if g<10:
        ret += "0"
    if g<255:
        ret += str(hex(g)).upper()[2:4] 
        ret+= "FF"
    if b<10:
        ret += "0"
    if b<255:
        ret += str(hex(b)).upper()[2:4] 
    else:
        ret+= "FF"
    return ret
print(rgb(234,362,216))
