
def cube(n):
    ret = ""
    for i in range(n):
        print(" "*(n-1-i),"/\\"*(i+1),end="")
        ret = ret+" "*(n-1-i),"/\\"*(i+1)
        print("_\\"*n)
        ret = ret+"_\\"*n+"\n"
    for i in range(n):
        print(" "*(i),"\\/"*(n-i),end="")
        ret = ret+" "*(i),"\\/"*(n-i)
        print("_/"*n)
        ret = ret+"_/"*n+"\n"
    return
resultado_cube = cube(4)
print(resultado_cube)
