import plotly
import re
import plotly.plotly as py
import plotly.graph_objs as go
import HorariosQueFunciona2 as HQ

atomos = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","#","$","%","@","!"]
A = "(((A+(D+G))*(((B+(E+H))*(C+(F+I)))*((A>(-B*-C))*(B>(-A*-C)))))*(((((C>(-A*-B))*(D>(-E*-F)))*((E>(-D*-F))*(F>(-D*-E))))*(((G>(-H*-I))*(H>(-G*-I)))*((I>(-G*-H))*(A>(-D*-G)))))*((((D>(-A*-G))*(G>(-A*-D)))*((B>(-E*-H))*(E>(-B*-H))))*(((H>(-B*-E))*(C>(-F*-I)))*((F>(-C*-I))*(I>(-C*-F)))))))"

m1 = "((A+(B+C))>(((-f*-y)*(((-1*-k)*(-M*-6))*((-o*-Q)*(-#*-b))))*(((((-u*-W)*(-p*-R))*((-$*-c)*(-v*-X)))*(((-h*-J)*(-3*-m))*((-Ñ*-8)*(-q*-S))))*((((-%*-i)*(-K*-4))*((-e*-x)*(-Z*-j)))*(((-L*-5)*(-ñ*-P))*((-0*-s)*(-U*-!)))))))"
m2 = "((D+(E+F))>(-a*(((((-t*-V)*(-f*-y))*((-1*-k)*(-M*-6)))*(((-o*-Q)*(-#*-b))*((-u*-W)*(-m*-Ñ))))*((((-8*-d)*(-w*-Y))*((-n*-O)*(-9*-r)))*(((-T*-@)*(-ñ*-P))*((-0*-s)*(-U*-!)))))))"
m3 = "((G+(H+I))>(-f*(((((-y*-1)*(-g*-z))*((-2*-l)*(-N*-7)))*(((-p*-R)*(-$*-h))*((-J*-3)*(-m*-Ñ))))*((((-8*-q)*(-S*-%))*((-i*-K)*(-4*-j)))*(((-L*-5)*(-ñ*-P))*((-0*-s)*(-U*-!)))))))"
mtotal = "(" + m1 + "*(" + m2 + "*" + m3 + "))"
# r1 = "(((a+b)+(c+d))+((e+f)+(g+h)))+(((i+j)+(k+l))+((m+n)+(ñ+o))+((p+q)+(r+s)))"
# r2 = "(((t+u)+(v+w))+((x+y)+(z+J)))+(((K+L)+(M+N))+((Ñ+O)+(P+Q))+((R+S)+(T+U)))"
# r3 = "(((V+W)+(X+Y))+((Z+1)+(2+3)))+(((4+5)+(6+7))+((8+9)+(0+#))+(($+%)+(@+!)))"

r1 = "(((((((((((((((((((a+b)+c)+d)+e)+f)+g)+h)+i)+j)+k)+l)+m)+n)+ñ)+o)+p)+q)+r)+s)"
r2 = "(((((((((((((((((((t+u)+v)+w)+x)+y)+z)+J)+K)+L)+M)+N)+Ñ)+O)+P)+Q)+R)+S)+T)+U)"
r3 = "(((((((((((((((((((V+W)+X)+Y)+Z)+1)+2)+3)+4)+5)+6)+7)+8)+9)+0)+#)+$)+%)+@)+!)"
rtotal =  r1 +"*"+ r2
rtotaltotal = rtotal +"*"+ r3
FORMULA = "(" + A + "*" + mtotal + ")"
TOTAL = "("+FORMULA + "*" + rtotaltotal+")"
#TOTAL = "("+ TOTAL + "*-a)"
interps= {}

A = HQ.String2List(TOTAL)
print("ESTO ES STRING 2 LIST DE A: \n")
print(A)
print("------------------------------------------")
B = HQ.tseitin(A, atomos)
print("ESTO ES TSEITIN: \n")
print(B)
print("-------------------------------------------")
S = HQ.List2String(B)
print("ESTO ES LIST 2 STRING: \n")
print(S)
print("--------------------------------------------")
Eq = HQ.equivalencias(S)
print("ESTO ES EQUIVALENCIAS: \n")
print(Eq)
print("-------------------------------------------")
formulaconjuntiva = HQ.clausulas("[" + Eq + "]")
print("ESTO ES CLAUSULAS: ")
print()
print(formulaconjuntiva)
print()

formula = []
for i in formulaconjuntiva:
    stra = ""
    for j in i:
        stra += j
    formula.append(stra)

print(formula)
interps = HQ.DPLLResultado(formula)
interpsFinal = {}
for i in interps:
    if i in atomos:
        interpsFinal[i] = interps[i]
    elif i[0] == '-':
        if i[1:] in atomos:
            interpsFinal[i] = interps[i]

print(interpsFinal)

tabla=["A","B","C","D","E","F","G","H","I"]

formulafinal = []
if interpsFinal:
    for i in interpsFinal:
        if interpsFinal[i] == 1:
            formulafinal.append(i)
        else:
            formulafinal.append("-"+i)
print(formulafinal)

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

def tabular(final):
    #La tabla es generada como un archivo en plot.ly en un respectivo usuario. En este ejemplo usamos el usuario y la llave
    #de Isabella, pero si se desea, se puede usar cualquier usuario en plot.ly cambiando la siguiente información:
    plotly.tools.set_credentials_file(username='BelisaDi', api_key='rjQlbw3URviMOZxB5eGP')
    trace = go.Table(
        header=dict(values=['Monitor', 'Cálculo 1','Lógica','Pensamiento']),
        cells=dict(values=[['Pablo', 'Sergio', 'Laura'],
                        [final[0],final[3] ,final[6]],[final[1],final[4],final[7]],[final[2],final[5],final[8]]]))
    data = [trace]
    py.plot(data, filename = 'Monitores PRUEBA')
final = llenar(tabla,formulafinal)
#tabular(final)
