import random

def busqueda_binaria(lista,comienzo,final,objetivo):
    
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2
    #print(f'medio = {medio}, comienzo = {comienzo}, final = {final}')
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        #print(f'lista medio menor = {lista[medio]}')
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        #print(f'lista medio mayor = {lista[medio]}')
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
    
if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista ?'))
    objetivo = int(input('Que numero quieres encontrar ?'))
    
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista,0,len(lista), objetivo)
    
    print(lista)
    print(f'El elemento {objetivo} { "esta" if encontrado else "no esta"} en la lista')