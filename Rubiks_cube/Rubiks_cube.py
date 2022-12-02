
def cube(n):
    ret = ""
    for i in range(n):
        ret = (ret + " "*(n-1-i)+"/\\"*(i+1))
        ret = (ret + "_\\"*n+"\n")
    for i in range(n):
        ret = (ret + " "*(i)+"\\/"*(n-i))
        ret = (ret + "_/"*n)
        if i !=n-1: #si la i no esta en el valor mete un intro ("\n")
            ret = ret+"\n" 
    return ret
resultado_cube = cube(4)
print(resultado_cube)
