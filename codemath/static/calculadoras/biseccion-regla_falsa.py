from math import*
from pylab import *
from numpy import *

class Biseccion:

    def funcion_evaluada(x):
    return eval(funcion)

    def biseccionraiz(funcion_evaluada,a,b,errort):
        
        if (funcion_evaluada(a)>0 and funcion_evaluada(b) <0) or (funcion_evaluada(a)<0 and funcion_evaluada(b)>0):
            raiz=a
            cont=0
            merr=[]
            merr.insert(0,0)
            error=1
            i=0
            while abs(error)>errort and cont<=100:
                raiz=(a+b)/2
                merr.append(raiz)
                if funcion_evaluada(a)*funcion_evaluada(raiz)<0:
                    b=raiz
                else:
                    a=raiz
                cont=cont+1
                i=i+1
                error=(merr[i]-merr[i-1])/merr[i]
                print(str(cont)+","+str(raiz))
                print("Error: ",abs(error))
            return raiz
        else:
            return 'no es menor que 0 no toca el eje x no hay raiz '

class Regla_falsa:
    def funcion_evaluada(x):
    return eval(funcion)

    def regla_falsaraiz(funcion_evaluada,lim1,lim2,errort):
        cont=0
        raiz=0
        merr=[]
        merr.insert(0,0)
        error=1
        i=0
        while cont<=100 and abs(error)>errort:
            if funcion_evaluada(lim1) * funcion_evaluada(lim2) < 0 :
                raiz = lim2 - (funcion_evaluada(lim2) * (lim2-lim1)) / (funcion_evaluada(lim2) - funcion_evaluada(lim1))
                merr.append(raiz)
                if funcion_evaluada(lim1) * funcion_evaluada(raiz) < 0:
                    lim2 = raiz
                else:
                    lim1 = raiz
                cont=cont+1
                i=i+1
                error=(merr[i]-merr[i-1])/merr[i]
                print(str(cont)+","+str(raiz))
                print("Error: ",abs(error))
            else:
                return 'no es menor que 0 no toca el eje x no hay raiz'
        return raiz
         






funcion = input('funcion: ')
a= float(input('limite superior a del intervalo: '))
b = float(input('limite inferior b del intervalo: '))
errort = float(input('ingrese erro de tolerancia: '))



raiz_biseccion = biseccion (funcion_evaluada,a,b,errort)
print ('raiz por el metodo de biseccion es: ', raiz_biseccion)
raiz_regla_falsa = regla_falsa (funcion_evaluada,a,b,errort)
print ('raiz por el metodo de regla falsa es: ', raiz_regla_falsa)

"""x=arange(a,b,errort*10)
y=eval(funcion)
plot(x,y,'b-',raiz_biseccion,funcion_evaluada(raiz_biseccion),'r:o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Biseccion ")
plt.text(raiz_biseccion,funcion_evaluada(raiz_biseccion),'raiz')
plt.grid(True)
plt.show()

x=arange(a,b,errort*10)
y=eval(funcion)
plot(x,y,'b-',raiz_regla_falsa,funcion_evaluada(raiz_regla_falsa),'r:o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Regla falsa funcion:")
plt.text(raiz_regla_falsa,funcion_evaluada(raiz_regla_falsa),'raiz')
plt.grid(True)
plt.show()  
    
"""

