import re

def regla3(monitores):
    monitorias=[]
    idx=0
    idx2=0
    horario=["atV","fy1","kM6","oQ#","buW","gz2","lN7","pR$","cvX","hJ3","mÑ8","qS%","dwY","iK4","nO9","rT@","exZ","jL5","ñP0","sU!"]
    for i in monitores:
        monitorias.append([])
        idx2=0
        for p in i:
            if(p=="0"):
                stra="-"+horario[idx2][0]+"*"+"-"+horario[idx2][1]+"*"+"-"+horario[idx2][2]+"*"
                monitorias[idx].append(stra)
            idx2+=1
        idx+=1
    m1="(A*(B*C))>("
    m2="(D*(E*F))>("
    m3="(G*(H*I))>("
    for i in range(len(monitorias[0])):
        m1+=monitorias[0][i]
    for i in range(len(monitorias[1])):
        m2+=monitorias[1][i]
    for i in range(len(monitorias[2])):
        m3+=monitorias[2][i]
    m1+=")"
    m2+=")"
    m3+=")"
    final=m1+"*"+m2+"*"+m3
    final2 = final.replace("*)",")")
    return final2

def equi(f):
    if f[1][0]=="-":
        final="(-"+f[0]+"+"+f[1]+")*("+f[0]+"+-"+f[1]+")"
        return final
    else:
        if f[1].find("*")>=0:
            idx=f[1].find("*")
            p=f[0]
            q=f[1][0:idx]
            r=f[1][idx+1:]
            final="("+q+"+"+"-"+p+")*("+r+"+"+"-"+p+")*(-"+q+"+"+"-"+r+"+"+p+")"
        elif f[1].find("+")>=0:
            idx=f[1].find("+")
            p=f[0]
            q=f[1][0:idx]
            r=f[1][idx+1:]
            final="(-"+q+"+"+p+")*(-"+r+"+"+p+")*("+q+"+"+r+"+-"+p+")"
        elif f[1].find(">")>=0:
            idx=f[1].find(">")
            p=f[0]
            q=f[1][0:idx]
            r=f[1][idx+1:]
            final="("+q+"+"+p+")*(-"+r+"+"+p+")*(-"+q+"+"+r+"+-"+p+")"
            return final
    return final

def equivalencias(formula):
    idx = formula.find("*")+1
    parentesis=0
    final=formula[0:idx-1]
    f=["",""]
    ignorar=False
    idx2=0
    for i in range(idx,len(formula)):
        if(ignorar):
            ignorar=False
            continue
        elif(formula[i]=="(" ):
            parentesis+=1
        elif(formula[i]==")"):
            parentesis-=1
            if(parentesis==0):
                idx2=0
                tmp="*"+(equi(f))
                final+=tmp
                f=["",""]
                ignorar=True
        elif(formula[i]=="="):
            idx2 += 1;
        else:
            f[idx2]+=formula[i]
    final2 = final.replace("--","")
    return final2

def tseitin(A, atomos):
    listax = []
    for i in range(1,500):
        listax.append(chr(i+10000))
    l = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if(s in atomos and len(pila) > 0 and pila[-1]== '-'):
            i += 1
            atomo = listax[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(["(", atomo, "=", "-"+s , ")"])
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif(s==')'):
            w=pila[-1]
            o=pila[-2]
            v=pila[-3]
            pila = pila[:len(pila)-4]
            i+=1
            atomo = listax[i]
            l.append(["(", atomo, "=", "(", v, o, w, ")",")"])
            s=atomo
        else:
            pila.append(s)
            A=A[1:]
            if(len(A)>0):
                s=A[0]
    B = []
    l.reverse()

    if i < 0:
        atomo = pila[-1]
    else:
        atomo = listax[i]
    for x in l:
        y = x
        B.append("*")
        for f in y:
            B.append(f)
    B = [atomo] + B
    return B

def List2String(list):
    stra = "";
    for x in list:
        stra += x
    return stra

def String2List(stra):
    list = []
    for x in stra:
        list.append(x)
    return list;

def clausulas(formula):
    clausulasFinales=[]
    tmp=[]
    string=""
    idx=formula.find("*")
    clausulasFinales.append([formula[1:idx]])
    for i in formula[idx+1:]:
        if(i=="+"):
            tmp.append(string)
            string=""
        elif(i=="*" or i=="]"):
            tmp.append(string)
            clausulasFinales.append(tmp)
            string=""
            tmp=[]
        elif(i!="(" and i!=")"):
            string += i
    return clausulasFinales

def clausulaUnitaria(lista) :
    for i in lista:
        if (len(i)==1):
            return i
        elif (len(i)==2 and i[0]=="-"):
            return i
    return None

def clausulaVacia(lista):
    for i in lista:
        if(i==''):
            return(True)
    return False

def unitPropagate(lista,interps):
    x = clausulaUnitaria(lista)
    while(x!= None and clausulaVacia(lista)!=True):
        if (len(x)==1):
            interps[str(x)]=1
            j = 0
            for i in range(0,len(lista)):
                lista[i]=re.sub('-'+x,'',lista[i])
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
        else:
            interps[str(x[1])]=0
            j = 0
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
            for i in range(0,len(lista)):
                lista[i]=re.sub(x[1],'',lista[i])
        x = clausulaUnitaria(lista)
    return(lista, interps)

def literal_complemento(lit):
    if lit[0] == "-":
        return lit[1]
    else:
        lit = "-" + lit
        return lit

def DPLL(lista, interps):
    lista, interps = unitPropagate(lista,interps)
    if(len(lista)==0):
        listaFinal = lista
        interpsFinal = interps
        return(lista,interps)
    elif("" in lista):
        listaFinal = lista
        interpsFinal = interps
        return (lista,{})
    else:
        listaTemp = [x for x in lista]
        for l in listaTemp[0]:
            if (len(listaTemp)==0):
                return (listaTemp, interps)
            if (l not in interps.keys() and l!='-'):
                break
        listaTemp.insert(0,l)
        lista2, inter2 = DPLL(listaTemp, interps)
        if inter2 == {}:
            listaTemp = [x for x in lista]
            a =literal_complemento(l)
            listaTemp.insert(0,a)
            lista2, inter2 = DPLL(listaTemp, interps)
        return lista2, inter2

def DPLLResultado(lista):
    lista, inter = DPLL(lista,{})
    return inter
