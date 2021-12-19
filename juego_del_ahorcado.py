
import random
import unicodedata
import os

#Función que toma como entrada la letra, palabra y los espacios en blanco iniciales "_ _ _", hace una busqueda y si la letra ingresada está en la palabra, retorna los espacios modificados: "A _ _":
def imprime_juego(letra, palabra, espacios):
    l_text = list(espacios)
    
    for i in range(0, len(palabra)):
        if letra == palabra[i]:
            l_text[i*2]= letra
            espacios="".join(l_text)

    return espacios

#Función que tiene como entrada una letra y retorna una letra sin caracteres especiales, sin espacios y en mayusculas.
def quitar_caracteres(letra):
    a_letra = unicodedata.normalize('NFKD', letra).encode('ASCII', 'ignore').strip().upper() 
    letra_unicode = a_letra.decode('UTF-8')

    return letra_unicode

#Función principal
def run():
    #Leer datos de un .txt y pasarlos a una lista:
    my_list =[]
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for string in f:
            my_list.append(string)

    #List compreheisions para agregar a la lista solo los datos en mayusculas y quitando espacios: 
    my_list = [string.upper().rstrip("\n") for string in my_list]
      
    #Elegir una palabra aleatoria de la lista   
    aleatorio = random.randrange(0, len(my_list) - 1 )
    palabra = my_list[aleatorio]
    palabra_unicode = quitar_caracteres(palabra)
    palabra_buscada=""
    espacios="_ "*len(palabra)
  
    #Clean screen and print first message
    os.system("cls")

    print(
        "██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗"+"\n"+
        "██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝"+"\n"+
        "███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║  ██║░░██╗░███████║██╔████╔██║█████╗░░"+"\n"+
        "██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░"+"\n"+
        "██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗"+"\n"+
        "╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"+"\n")
    
    print("¡Adivina la palabra!")
    print("\n")
    print(espacios)
    print("\n")

    #Mientras la palabra escogida sea diferente de la palabra_buscada, entonces solicite una letra hasta que las palabras sean iguales:

    while palabra_buscada != palabra_unicode:
        
        letra = input("Ingrese una letra: ")
        letra_unicode = quitar_caracteres(letra)
        espacios = imprime_juego(letra_unicode,palabra_unicode, espacios)
        palabra_buscada = espacios.replace(" ","")
        os.system("cls")
        print(
        "██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗"+"\n"+
        "██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝"+"\n"+
        "███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║  ██║░░██╗░███████║██╔████╔██║█████╗░░"+"\n"+
        "██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░"+"\n"+
        "██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗"+"\n"+
        "╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"+"\n")
        print("¡Adivina la palabra!")
        print("\n")
        print(espacios)
        print("\n")

    print(
    "█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █░█ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀ █ "+"\n"+ 
    "█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█ ▄ "+"\n"+"\n"+

    "█▄█ █▀█ █░█   █░█░█ █▀█ █▄░█   ▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀"+"\n"+
    "░█░ █▄█ █▄█   ▀▄▀▄▀ █▄█ █░▀█   ░█░ █▀█ ██▄   █▄█ █▀█ █░▀░█ ██▄")
    
       
if __name__ == "__main__":
    run()