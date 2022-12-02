def alphabet_war(fight):
    left = {"w" : 4,"p" : 3,"b" : 2,"s" : 1} # hacemos un diccionario con las letras de cada side y sus valores
    right = {"m" :4,"q" : 3,"d" : 2,"z" : 1}
    count_left = 0 #le asignamos un valor inicial igual a 0
    count_right = 0
    for i in fight: #para cada elemento de fight, vemos si esta en left o esta en right
        if i in left:
            count_left += left[i] #se le suman los puntos de las letras definidas en left
        elif i in right:
            count_right += right[i]
    if count_right < count_left:
        return "Left side wins!"
    elif count_right > count_left:
        return "Right side wins!"
    else:
        return "Let's fight again!"

print(alphabet_war("zdqmwppbs"))
