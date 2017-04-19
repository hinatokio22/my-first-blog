from math import*
#from sympy.solvers import solve
#from sympy import Symbol
#from pylab import *
#from numpy import *

class Bisec:

    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def biseccionraiz(self,funcion,a,b,errort):
        m=Bisec()
        if (m.funcion_evaluada(float(a),funcion)>0 and m.funcion_evaluada(float(b),funcion) <0) or (m.funcion_evaluada(float(a),funcion)<0 and m.funcion_evaluada(float(b),funcion)>0):
            raiz=a
            cont=0
            merr=[]
            merr.insert(0,0)
            error=1
            i=0
            while abs(error)>errort and cont<=100:
                raiz=(a+b)/2
                merr.append(raiz)
                if m.funcion_evaluada(float(a),funcion)*m.funcion_evaluada(float(raiz),funcion)<0:
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

    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def regla_falsaraiz(self,funcion,lim1,lim2,errort):
        cont=0
        raiz=0
        merr=[]
        merr.insert(0,0)
        error=1
        i=0
        m=Bisec()
        while cont<=100 and abs(error)>errort:
            if m.funcion_evaluada(float(lim1),funcion) * m.funcion_evaluada(float(lim2),funcion) < 0 :
                raiz = lim2 - (m.funcion_evaluada(float(lim2),funcion) * (lim2-lim1)) / (m.funcion_evaluada(float(lim2),funcion) - m.funcion_evaluada(float(lim1),funcion))
                merr.append(raiz)
                if m.funcion_evaluada(float(lim1),funcion) * m.funcion_evaluada(float(raiz),funcion) < 0:
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

class Secantec:

    def __init__(self):
        return

    def f(self,x,funcion):
        return eval(funcion)


    def secantef(self,funcion,x1,x0,error):
         itera=0
         i=0
         raiz=[]
         raiz.insert(0,0)
         erro=1
         m=Secantec()
         while(i<=100 and abs(erro)>error):
             x2=x1-(m.f(x1,funcion)*(x1-x0))/(m.f(x1,funcion)-m.f(x0,funcion))
             raiz.append(x2)
             x0=x1
             x1=x2
             itera=itera+1
             i=i+1
             erro=(raiz[i]-raiz[i-1])/raiz[i]
             print(itera,". ",x2)
             print("Error: ",abs(erro))
         return x2

class Polin:

    def __init__(self):
        return

    def raizPolinomios(self,funcion):
        x=Symbol('x')
        raices=solve(funcion,x)
        return raices

class Evalu:
    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def evalua(self,x,funcion):
        m=Evalu()
        res=m.funcion_evaluada(x,funcion)
        return res

class Deriv:
    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def derivada(self,fun):
        return diff(fun)

    def derivando(self,x,funcion):
        m=Deriv()
        newfun=str(m.derivada(funcion))
        res=m.funcion_evaluada(x,newfun)
        return res

class Simp13:

    def __init__(self):
        return

    def fx(self,x, f):
        return eval(f)

    def simpin13(self,n, a, b, f):
        m=Simp13()
        h = (b - a) / n
        suma = 0.0
        for i in range(1, n):
            x = a + i * h
            if(i % 2 == 0):
                suma = suma + 2 * m.fx(x, f)
            else:
                suma = suma + 4 * m.fx(x, f)
        suma = suma + m.fx(a, f) + m.fx(b, f)
        rest = suma * (h / 3)
        return (rest)
