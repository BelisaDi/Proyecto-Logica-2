#-*-coding: utf-8-*-
# Jhan Carlos Celi Maldonado && Isabella Martinez Martinez, Abril/23/2018

# Visualizacion de las las monitorias con sus correspondientes monitores a partir de
# una lista de literales. Cada literal representa qué monitor dicta que monitoria;
# el literal es positivo si y solo si el monitor x dicta la monitoria y.

# Formato de la entrada: - las letras proposionales serán: A,B,C,D,E,F,G,H,I;
#                        - solo se aceptan literales (ej. -A, B, -C, D, etc.)
# Requiere también un string que guarde los valores finales de las casillas.

# importando librerías y paquetes para tabular
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#función que devuelve un string que posee el estado del tablero
def llenar(tabla,lista):
    final=""
    for i in tabla:
        for p in lista:
            if i==p:
                final+="x"
                break
            if lista[len(lista)-1]==p:
                final+=" "
    return final

#función que tabula los valores del string de salida
def tabular(final):
    #La tabla es generada como un archivo en plot.ly en un respectivo usuario. En este ejemplo usamos el usuario y la llave
    #de Isabella, pero si se desea, se puede usar cualquier usuario en plot.ly cambiando la siguiente información:
    plotly.tools.set_credentials_file(username='BelisaDi', api_key='rjQlbw3URviMOZxB5eGP')
    trace = go.Table(
        header=dict(values=['Monitor', 'Cálculo 1','Lógica','Pensamiento']),
        cells=dict(values=[['Pablo', 'Sergio', 'Laura'],
                        [final[0],final[3] ,final[6]],[final[1],final[4],final[7]],[final[2],final[5],final[8]]]))
    data = [trace]
    py.iplot(data, filename = 'Monitores 2')

#lista de literales (input)
lista=["A","-B","C","D","-E","F","-G","H","I","M","N","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","#","@","!"]
#lista que representa las posiciones de la tabla
tabla=["A","B","C","D","E","F","G","H","I"]
#string de salida que guardara el estado de la tabla
final = llenar(tabla,lista)
#tabula los valores del string final
tabular(final)
