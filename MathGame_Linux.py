import random
import tkinter
from tkinter import *
import PIL
from PIL import ImageTk, Image, ImageDraw, ImageFont
import statistics
from statistics import mode 


"""
Función imagen: nos ayuda principalmente para el primer grado de primaria, interactuando con archivos, los cuales se encuentran enumerados.

Si usted desea quitar o añadir más ejercicios, puede hacerlo fácilmente, modificando la carpeta con las imágenes y el código, y el rango del atributo p. 

El rango de P, es un número aleatorio entre el número de imágenes existentes.
"""
def imagen(p,tem,grado):
    if grado == 1:
        g = "Grado_1"
        if tem == 1:
            z = "~Aprende a contar~"
            m = "contar"
        elif tem == 2:
            z = "~Aprende a sumar~"
            m = "sumar"
        elif tem == 3:
            z = "~Aprende a restar~"
            m = "restar"
    x = str(p)
    x+=".png"
    ventana = Tk()
    ventana.geometry("+0+0")
    ventana.title(f"{z}")
    imagen = ImageTk.PhotoImage(Image.open(rf"img/{g}/{m}/{x}"))
    label = Label(image=imagen)
    label.pack()
    ventana.mainloop()

"""
NOTA: Las funciones de los grados cuentan con dos apartados: * Llamadas por la función reto: Aquí será igual a 1, de esta manera estamos indicando que solo se efectuara 
una pregunta sobre un tema aleatorio en ese grado. *Llamadas por la función main: Se efectuará un número de preguntas random no menor a 10 y no mayor a 25, 
sobre el grado y tema seleccionados.
"""


"""
Función reto: En esta  función los random acceden a cada grado de manera aleatoria, ingresando a un apartado donde el grado genera todo de manera aleatoria
en un rango determinado, el cual también puede ser modificado.

El grado genera todo de forma aleatoria debido a que está programado de esta manera, a diferencia del modo aprendizaje, aquí no se le pregunta al usuario por cuál grado y tema desea jugar.

Se establecerá de forma aleatoria en cada iteración y si el usuario falla en su respuesta, se elimina el apartado que te indica, la respuesta correcta que está en el apartado aprendizaje.

Además, este apartado está con el fin de otorgarte un reconocimiento si al final tienes un promedio mayor o igual a 8, ya que estás poniendo a prueba tus conocimientos.
---- Se solicita el nombre del usuario al inicio.
"""
def reto(j):
    print("El modo de reto consiste en preguntas aleatorias de todos los grados.")
    print('Si saca un promedio mayor a 8 obtendrá un certificado. -- \b(*Podrá descargarlo*)\b')
    print("\nIngrese su nombre completo: ")
    no = input("==> ")
    while len(no) <= 5:
        no = input("==> ")
    no = no.capitalize()
    cont = 0
    p = random.randint(15,25)
    print(f"\nPREGUNTAS A REALIZAR => {p}")
    for x in range(p):
        print(f"\n#{x+1}")
        g = random.randint(1,6) 
        if g == 1:
            cont += primer_grado(g,j)
        elif g == 2:
            cont += segundo_grado(g,j)
        elif g == 3:
            cont += tercer_grado(g,j)
        elif g == 4:
            cont += cuarto_grado(g,j)
        elif g == 5:
            cont += quinto_grado(g,j)
        else:
            cont += sexto_grado(g,j)
    prom = (cont/p)*10
    print(f"\n~Respondiste bien {cont} de {p} preguntas.~")
    print(f"\n~Finalizaste con un promedio de {prom:.2f}.~")
    if prom >= 8:
        certificado(no)
    else:
        print(f"\nPuedes conseguir un mayor promedio!!")
        print(f"\nRECUERDA: Un promedio mayor a 8 te otorga tu reconocimiento =D\n")


"""
Función certificado: Esta función es la que accede el certificado y lo muestra con ayuda de la librería PIL, ingresando el nombre del usuario que fue pedido antes.

Este se acomoda en la imagen mediante píxeles, es por ello que dependiendo del número de letras que tenga la Sting, ya que todos los nombres no son iguales,
se acomodara de forma diferente, quedando centrado.
"""
def certificado(ni):
    l = len(ni)
    img = Image.open(rf"img/Reto/certificado/1.png")
    draw = ImageDraw.Draw(img)
    if l <= 10:
        x = 685
    elif l <= 24:
        x = 465
    elif l <= 30:
        x = 385
    elif l > 30:
        x = 270
    font= ImageFont.truetype(r"Fonts/Gabriola.ttf",100)
    draw.text((x,510), f"{ni}", fill="black", font=font)
    img.show()


"""
Función primer_grado: Este grado interactúa con las imágenes para mostrar ejercicios matemáticos básicos, accediendo a ellos de manera aleatoria.

Además, llama a la función respuestas donde se encuentran las matrices, donde se almacena todo el material de apoyo en matrices y se accede a él con base en el grado 
y tema seleccionado. 

En la función de respuestas también está programado todo el funcionamiento en cuanto funcionamiento y cálculo de los ejercicios, para que se pueda acceder fácilmente 
a los datos y comprobar la respuesta en el momento que se ingresa la respuesta del usuario.
"""
def primer_grado(g,j):
    if j == 2:
        print("\n~NOTA~\n")
        print("~ESTE GRADO ES CON IMÁGENES, LEA LA PREGUNTA, VEA LA IMAGEN Y LUEGO CIÉRRELA PARA RESPONDER~\n")
        print("Seleccione su tema:\n")
        print(" 1◉ Aprende a contar\n 2◉ Aprende a sumar\n 3◉ Aprende a restar\n")
        print("NOTA: ingrese solo el número del tema.")
        tema = int(input("==> "))
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            n = random.randint(1,20)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"¿Cuántos {l} hay en la imagen?")
            elif tema == 2:
                print(f"¿Cuánto es {l}?")
            else:
                print(f"¿Cuánto es {l}?")
            imagen(n,tema,g)
            con = int(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(\n")
                print(f"Respuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        k = 1
        for x in range(k):
            n = random.randint(1,20)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"¿Cuántos {l} hay en la imagen?")
            elif tema == 2:
                print(f"¿Cuánto es {l}?")
            else:
                print(f"¿Cuánto es {l}?")
            imagen(n,tema,g)
            con = int(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
Función segundo_grado: Este grado trabaja con listas, estas son creadas dentro de la función matriz_respuestas, donde se comprueban las respuestas mediante las matrices y 
retornando la respuesta correcta, así como el material de apoyo, que sería la lista en formato de Sting.
"""
def segundo_grado(g,j):
    if j == 2:
        print("Seleccione su tema:\n")
        print(" 1◉ Secuencias numéricas crecientes\n 2◉ Secuencias numéricas decrecientes\n 3◉ Encuentra el numéro faltante\n")
        print("NOTA: ingrese solo el numéro del tema.")
        tema = int(input("==> "))
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            n = random.randint(1,15) #Aumento en la secuencia y numero a sumar
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la secuencia {l} ¿que numéro falta?")
            elif tema == 2:
                print(f"En la secuencia {l} ¿que numéro falta?")
            else:
                print(f"En la suma {l} ¿que numéro falta?")
            con = int(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(\n")
                print(f"Respuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        cont = 0
        k = 1
        for x in range(k):
            n = random.randint(1,15)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la secuencia {l} ¿que numéro falta?")
            elif tema == 2:
                print(f"En la secuencia {l} ¿que numéro falta?")
            else:
                print(f"En la suma {l} ¿que numéro falta?")
            con = int(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
Función tercer_grado: Este grado genera todo de manera aleatoria, generando la respuesta dentro de la función matriz_respuestas, así como el material de apoyo, 
retornando dos valores, respuesta correcta y material de apoyo; comprobando todo dentro de la función para determinar si la respuesta que ingresa el usuario es correcta.
"""
def tercer_grado(g,j):
    if j == 2:
        print("\nSeleccione su tema:\n")
        print(" 1◉ Aprende a multiplicar\n 2◉ Aprende a dividir\n 3◉ Aprende a reconocer el numéro mayor\n")
        print("NOTA: ingrese solo el numero del tema.")
        tema = int(input("==> "))
        if tema == 2:
            print("\nNOTA: si su respuesta tiene 2 o más decimales, ingrese solo 2.")
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            if tema == 2:
                n = random.randrange(10,20,2)
            else:
                n = random.randint(1,10)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"¿Cuánto es {l}?")
                con = int(input("==> "))
            elif tema == 2:
                m = round(m,2)
                print(f"¿Cuánto es {l}?")
                con = float(input("==> "))
            else:
                j = p[2]
                print(f"¿Cuál numéro es mayor {l} o {j} ?")
                con = int(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
                print(f"\nRespuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        if tema == 2:
            print("\nNOTA: si su respuesta tiene 2 o más decimales, ingrese 2 decimales.\n")
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        k = 1
        for x in range(k):
            if tema == 2:
                n = random.randrange(10,20,2)
            else:
                n = random.randint(1,10)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"\n¿Cuánto es {l}?")
                con = int(input("==> "))
            elif tema == 2:
                m = round(m,2)
                print(f"\n¿Cuánto es {l}?")
                con = float(input("==> "))
            else:
                j = p[2]
                print(f"\n¿Cuál numero es mayor {l} o {j} ?")
                con = int(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
Función cuarto_grado: Este grado cuenta con 3 figuras ya predeterminadas para sacar su área, además se generaran los valores necesarios para sacar el área de forma aleatoria 
y se realizara el cálculo a la vez en la función matriz_repsuestas, de esta manera cuando el usuario ingrese su respuesta se comprobará automáticamente.

Las figuras están representadas mediante '*' acomodados en  una lista, estas no son de forma aleatoria, sino pre configurado para que se vea correctamente representada 
la forma de la figura.
"""
def cuarto_grado(g,j):
    if j == 2:
        print("Seleccione su tema:\n")
        print(" 1◉ Áreas de cuadrados\n 2◉ Áreas de rectángulos\n 3◉ Áreas de triángulos\n")
        print("NOTA: ingrese solo el número del tema.")
        tema = int(input("==> "))
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            n = random.randint(1,20) #Lado o Altura de figura
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                lista = ["*********","*       *","*       *","*       *","*********"]
                print("Para el cuadrado: \n")
                for x in lista:
                    print(x)
                print(f"\nLa fórmula es: Lado x Lado = Area\n")
                print(f"sus lados miden {l} cm.\n")
                print("\b¿Cuál es su área?\b")
            elif tema == 2:
                print("Para el rectángulo: \n")
                lista = ["**************","*            *","*            *","*            *","**************"]
                for x in lista:
                    print(x)
                print(f"\nLa fórmula es: Base x Altura = Area\n")
                print(f"\nSu altura {l}.\n")
                print("\b¿Cuál es su área?\b")
            else:
                m = round(m,2)
                print("Para el triángulo: \n")
                lista = ["   *","  * *"," *   *","*     *","********"]
                for x in lista:
                    print(x)
                print(f"\nLa fórmula es: (Base x Altura) / 2 = Area\n")
                print("\nNOTA: si su respuesta tiene 2 o más decimales, ingrese 2 decimales.\n")
                print(f"Su altura mide {l} cm.\n")
                print("\b¿Cuál es su área?\b")
            con = float(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(\n")
                print(f"Respuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        cont = 0
        k = 1
        for x in range(k):
            n = random.randint(1,20)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                lista = ["*********","*       *","*       *","*       *","*********"]
                print("Para el cuadrado: \n")
                for x in lista:
                    print(x)
                print(f"sus lados miden {l} cm.\n")
                print("\b¿Cuál es su área?\b")
            elif tema == 2:
                print("Para el rectángulo: \n")
                lista = ["**************","*            *","*            *","*            *","**************"]
                for x in lista:
                    print(x)
                print(f"\nSu altura {l}.\n")
                print("\b¿Cuál es su área?\b")
            else:
                m = round(m,2)
                print("Para el triángulo: \n")
                lista = ["   *","  * *"," *   *","*     *","********"]
                for x in lista:
                    print(x)
                print("\nNOTA: si su respuesta tiene 2 o más decimales, ingrese 2 decimales.\n")
                print(f"Su altura mide {l} cm.\n")
                print("\b¿Cuál es su área?\b")
            con = float(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
Función quinto_grado: Este grado trabaja con la generación de números decimales.

En los primeros dos temas se trabaja realizando las operaciones correspondientes al momento de generar los números, para tener así la respuesta para su comprobación.

En el tercer tema, que es encontrar el número faltante, se trabaja con una lista, para así aleatoriamente tomar una posición e ingresar "---" para indicarte el número que tienes que encontrar.

Todo es generado dentro de la función matriz y comprobado en la función de quinto_grado.
"""
def quinto_grado(g,j):
    if j == 2:
        print("Seleccione su tema:\n")
        print(" 1◉ Suma con decimales\n 2◉ resta con decimales\n 3◉ Encuentra el numéro faltante-Multiplicación\n")
        print("NOTA: ingrese solo el numero del tema.")
        tema = int(input("==> "))
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            n = random.randint(1,15) #Aumento en la secuencia y numero a sumar
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la suma {l} ¿Cuál es el resultado?")
            elif tema == 2:
                print(f"En la resta {l} ¿Cuál es el resultado?")
            else:
                print(f"En la multiplicación {l} ¿Qué número falta?")
            con = float(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(\n")
                print(f"Respuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        cont = 0
        k = 1
        for x in range(k):
            n = random.randint(1,15)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la suma {l} ¿Cuál es el resultado?")
            elif tema == 2:
                print(f"En la resta {l} ¿Cuál es el resultado?")
            else:
                print(f"En la multiplicación {l} ¿Qué número falta?")
            con = float(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
Función sexto_grado: Esta función trabaja con listas creadas de forma aleatoria mediante el apoyo de la librería random, todas las listas son creadas dentro de la función 
matriz_respuestas, convertidas a string para mostrarse al usuario, además mostradas ordenadas de menor a mayor a excepción de cuando se verifica la moda, ya que ahí finalmente 
se agrega un dato de forma repetida y se hace un sufle con random, para tener la lista desordenada. 

Para la mediana y media, se generó un proceso de comprobación mediante un ciclo, para generar la respuesta, y para la moda se utilizó una librería, 
además se tomó una posición aleatoria para ese dato ingresarlo más veces en la lista y que hubiese repetición segura con un valor.
"""
def sexto_grado(g,j):
    if j == 2:
        print("Seleccione su tema:\n")
        print(" 1◉ Media/Promedio\n 2◉ Mediana\n 3◉ Moda\n")
        print("NOTA: ingrese solo el numero del tema.")
        tema = int(input("==> "))
        while not(tema >= 1 and tema <= 3):
            tema = int(input("==> "))
        cont = 0
        lista = []
        k = random.randint(10,20)
        for x in range(k):
            print(f"\n#{x+1}")
            n = random.randint(1,15) #Aumento en la secuencia y numero a sumar
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la lista {l} ¿Cuál es la media/promedio?")
            elif tema == 2:
                print(f"En la lista {l} ¿Cuál es la mediana?")
            else:
                print(f"En la lista {l} ¿Cuál es la moda?")
            con = float(input("==> "))
            lista.append(con)
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(\n")
                print(f"Respuesta correcta: {m}")
        print(f"\n~Respondiste bien {cont} de {k} preguntas.~")
        return lista
    elif j == 1:
        tema = random.randint(1,3)
        cont = 0
        k = 1
        for x in range(k):
            n = random.randint(1,15)
            p = matriz_respuestas(n,g,tema)
            l = p[0]
            m = p[1]
            if tema == 1:
                print(f"En la lista {l} ¿Cuál es la media/promedio?")
            elif tema == 2:
                print(f"En la lista {l} ¿Cuál es la mediana?")
            else:
                print(f"En la lista {l} ¿Cuál es la moda?")
            con = float(input("==> "))
            if con == m:
                print("Correcto!!")
                cont+=1
            else:
                print("Incorrecto:(")
        return cont


"""
La función matriz_respuestas, es el principal apoyo de todos los grados, ya que es donde se generan los datos, así como las respuestas mediante el uso de las matrices, 
dejando más fácil el manejo de los problemas si se desea editar o agregar más.

En cada tema, los if  crean exactamente las mismas variables, excluyendo en algunos casos algunas o modificando el tipo de variable, ya que no pueden no existir variables 
que están llamadas en una posición x de la matriz.

Al final, dependiendo del grado, los if acceden a los valores necesarios y los retornan al grado correspondiente o bien a la función reto.
"""
def matriz_respuestas(k,grado,tem):
    if grado == 1:
        r2 = 0
        lista = ""
        r1 = 0
        if tem == 1:
            p = 1
            j = ""
        elif tem == 2:
            p = 1
            j = ""
        elif tem == 3:
            p = 1
            j = 1
    elif grado == 2:
        r2 = 0
        p = 1 
        j = 1
        r1 = 0
        if tem == 1:
            lista=[]
            r1 = random.randint(0,10)
            for x in range(0,5,1):
                r1 += k
                lista.append(r1)
            r1 = len(lista)
            r1 = r1-1
            r1 = random.randint(0,r1)
            r2 = r1
            r1 = lista[r1]
            lista[r2] =  "---"
            lista = str(lista)
        elif tem == 2:
            k = random.randint(1,10)
            lista=[]
            r1 = random.randint(50,60)
            for x in range(0,5,1):
                r1 -= k
                lista.append(r1)
            r1 = len(lista)
            r1 = r1-1
            r1 = random.randint(0,r1)
            r2 = r1
            r1 = lista[r1]
            lista[r2] =  "---"
            lista = str(lista)
        elif tem == 3:
            lista = ""
            p = random.randint(1,20) #Numero a sumar
            j = p + k
            lista = [p, k]
            r2 = random.randint(1,2)
            r1 = lista[r2-1]
            lista[r2-1] = "---"
            lista = f"{lista[0]} + {lista[1]} = {j}"
    elif grado == 3:
        r2 = 0
        lista = ""
        r1 = 0
        if tem == 1:
            p = random.randint(1,10)
            j = f"{k} x {p}"
        elif tem == 2:
            p = random.randrange(2,10,2)
            j = f"{k} / {p}"
        elif tem == 3:
            p = random.randint(1,60)
            j = random.randint(1,50)
    elif grado == 4:
        r2 = 0
        lista = ""
        r1 = 0
        if tem == 1:
            r2 = k*k
            j = str(k)
            p = 1
        elif tem == 2:
            k = random.randint(1,15)
            p = random.randint(20,30)
            r2 = k*p
            j = f"mide {k} cm  y su base {p}"
        elif tem == 3:
            p = random.randint(1,20)
            k = p*2
            r2 = (k*p)/2
            j = f"mide {k} cm  y su base {p}"
    elif grado == 5:
        r2 = 0
        lista = ""
        r1 = 0
        if tem == 1:
            r1 = random.uniform(1,10)
            r2 = random.uniform(10,20)
            r1 = round(r1,1)
            r2 = round(r2,1)
            p = r1 + r2
            p = round(p,1)
            j = f"{r1} + {r2} = ---"
        elif tem == 2:
            r1 = random.uniform(1,10)
            r2 = random.uniform(10,20)
            r1 = round(r1,1)
            r2 = round(r2,1)
            p = r2 - r1
            p = round(p,1)
            j = f"{r2} - {r1} = ---"
        elif tem == 3:
            lista = ""
            p = random.randint(1,20) #Numero a sumar
            j = p * k
            lista = [p, k]
            r2 = random.randint(1,2)
            r1 = lista[r2-1]
            lista[r2-1] = "---"
            lista = f"{lista[0]} x {lista[1]} = {j}"
    elif grado == 6:
        r2 = 0
        lista = ""
        r1 = 0
        if tem == 1:
            #media
            lista=[]
            r1 = random.randint(0,10)
            for x in range(0,5,1):
                r1 += k
                lista.append(r1)
            r1 = sum(lista)/len(lista)
            lista = str(lista)
            j = ""
            p = 1
        elif tem == 2:
            #mediana
            lista=[]
            r1 = random.randint(0,10)
            p = random.randint(3,7)
            for x in range(0,p,1):
                r1 += k
                lista.append(r1)
            lista.sort()
            if (len(lista)%2 == 0):
                r1 = (len(lista)/2)
                r2 = int(r1)
                r1 = int(r1-1)
                r1 = lista[r1]
                r2 = lista[r2]
                r2 = (r1 + r2)/2
            else:
                r1 = (len(lista)/2)-0.5
                r1 = int(r1)
                r2 = lista[r1]
            lista = str(lista)
            j = ""
        elif tem == 3:
            #moda
            lista=[]
            r1 = random.randint(0,10)
            p = random.randint(3,4)
            for x in range(0,p,1):
                r1 += k
                lista.append(r1)
            for x in range(2):
                print(f"{x}")
                if x == 0:
                    print("ENTRO")
                    p = len(lista)
                    ri = random.randint(0,p-1)
                r1 = lista[ri]
                lista.append(r1)
            random.shuffle(lista)
            r2 = mode(lista)   
            lista = str(lista)
            j = ""
    
    #Textos o material de ayuda
    x = [[["changos","jugos","perros","oreos","conejos","muffins","lagartijas","pasteles","naranjas","fresas","platanos","manzanas","pingüinos","pingüinos","ositos","cerditos","gallos",
           "obejas","elefantes","lapices"],["5 + 2 circulitos","2 + 2 circulitos","5 + 3 circulitos","4 + 1 circulitos","6 + 3 circulitos","2 + 1 circulitos","6 + 4 serpientes",
        "2 + 8 nubes","5 + 1 gatos","7 + 2 lunas","1 + 1 muñecas","3 + 3 corazones","4 + 3 pentagonos","5 + 1 hexagonos","4 + 4 circulos","6 + 1 triangulos","2 + 4 estrellas",
        "2 + 6 cuadrados","3 + 4 pentagonos","6 + 3 rectangulos"],["6 - 1 estrellas de hielo","2 - 1 pingüino","3 - 1 corbatas","5 - 1 gorros","4 - 1 tazas","3 - 2 tortugas",
        "4 - 2 naves","7 - 5 pelotas","8 - 4 kit´s de playa","4 - 1 perros","3 - 1 coches","10 - 1 muñecas","8 - 6 barquitos","10 - 7 gallos","7 - 5 ositos","6 - 1 helicópteros",
        "10 - 9 cohetes","6 - 5 elefantes","7 - 4 ballenas","5 - 4 orugas"]],
         [[lista],[lista],[lista]],
         [[j],[j],[j]],
         [[j],[j],[j]],
         [[j],[j],[lista]],
         [[lista],[lista],[lista]]]
    #Respuestas o material de ayuda
    y = [[[3,7,4,6,7,4,1,2,6,7,4,5,8,6,3,6,4,3,5,6],[7,4,8,5,9,3,10,10,6,9,2,6,7,6,8,7,6,8,7,9],[5,1,2,4,3,1,2,2,4,3,2,9,2,3,2,5,1,1,3,1]],
         [[r1],[r1],[r1]],
         [[(k*p)],[k/p],[p]],
         [[r2],[r2],[r2]],
         [[p],[p],[r1]],
         [[r1],[r2],[r2]]]
    if grado == 1:
        if tem == 1:
            l=x[0][0][k-1]
            m=y[0][0][k-1]
        elif tem == 2:
            l=x[0][1][k-1]
            m=y[0][1][k-1]
        else:
            l=x[0][2][k-1]
            m=y[0][2][k-1]
        return(l,m)
    elif grado == 2:
        if tem == 1:
            l=x[1][0][0]
            m=y[1][0][0]
            return(l,m)
        elif tem == 2:
            l=x[1][1][0]
            m=y[1][1][0]
            return(l,m)
        else:
            l=x[1][2][0]
            m=y[1][2][0]
            return(l,m)
    elif grado == 3:
        if tem == 1:
            l=x[2][0][0]
            m=y[2][0][0]
            return(l,m)
        elif tem == 2:
            l=x[2][1][0]
            m=y[2][1][0]
            return(l,m)
        else:
            l=x[2][2][0]
            r=y[2][2][0]
            while l == r:
                r = random.randint(1,60)
                l = random.randint(1,50)
            m = l > r
            if m == True:
                m = l
            else:
                m = r
            return(l,m,r)
    elif grado == 4:
        if tem == 1:
            l=x[3][0][0]
            m=y[3][0][0]
            return(l,m)
        elif tem == 2:
            l=x[3][1][0]
            m=y[3][1][0]
            return(l,m)
        else:
            l=x[3][2][0]
            m=y[3][2][0]
            return(l,m)
    elif grado == 5:
        if tem == 1:
            l=x[4][0][0]
            m=y[4][0][0]
            return(l,m)
        elif tem == 2:
            l=x[4][1][0]
            m=y[4][1][0]
            return(l,m)
        else:
            l=x[4][2][0]
            m=y[4][2][0]
            return(l,m)
    else:
        if tem == 1:
            l=x[5][0][0]
            m=y[5][0][0]
            return(l,m)
        elif tem == 2:
            l=x[5][1][0]
            m=y[5][1][0]
            return(l,m)
        else:
            l=x[5][2][0]
            m=y[5][2][0]
            return(l,m) 


"""
Función main: Main es nuestro principal apoyo para el menú, ya que es donde todo empieza, dándote el primer menú con las primeras dos opciones, en total existen 8 menús 
diferentes, haciendo el juego más interactivo y entretenido.

Todo el código está muy en conjunto, puede ser modificado, pero si algo se modifica, muy probablemente tengas que modificar algo en otra función para el funcionamiento correcto.
"""  
def main():
    ren = "si"
    print("~BIENVENIDO A SUIFTY~\n~UN PROGRAMA DE APRENDIZAJE MATEMÁTICO~\n")
    while ren == "si":
        print("\n¿Qué modo desea jugar?")
        print("\n 1-Reto\n 2-Aprendizaje")
        jugar = int(input("==> "))
        while not (jugar >= 1 and jugar <= 2):
            jugar = int(input("==>"))
        matriz_r = []
        if jugar == 1:
            reto(jugar)
        else:
            print("Seleccione su grado:\n")
            print(" ◉ 1er grado\n ◉ 2do grado\n ◉ 3er grado\n ◉ 4to grado\n ◉ 5to grado\n ◉ 6to grado\n")
            print("NOTA: ingrese solo el número del grado.")
            grado = int(input("==> "))
            while not(grado >= 1 and grado <= 6):
                grado = int(input("==> "))
            if grado == 1:
                x = primer_grado(grado,jugar)
                matriz_r = [["Grado 1"],x]
            elif grado == 2:
                x = segundo_grado(grado,jugar)
                matriz_r = [["Grado 2"],x]
            elif grado == 3:
                x = tercer_grado(grado,jugar)
                matriz_r = [["Grado 3"],x]
            elif grado == 4:
                x = cuarto_grado(grado,jugar)
                matriz_r = [["Grado 4"],x]
            elif grado == 5:
                x = quinto_grado(grado,jugar)
                matriz_r = [["Grado 5"],x]
            else:
                x = sexto_grado(grado,jugar)
                matriz_r = [["Grado 6"],x]
        ren = input("\n¿Desea continuar aprendiendo?: ")
        ren = ren.lower()

main()
    
