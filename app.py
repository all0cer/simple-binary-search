def binarySearch(lista, item):
    inicio = 0
    final  = (len(lista)-1)
    meio = (inicio + final) // 2 
    while inicio <= final:
        if item == meio:
            return item
        if item < meio:
           return inicio - 1 
        else:
            return final + 1 
    return None

lista = [1,2,4,7,9,12]
res = binarySearch(lista, 12)
print(res)
