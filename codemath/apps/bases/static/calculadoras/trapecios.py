from math import*
import random




class Trapecios:
    
    def __init__(self):
        return
    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def trap(self,funcion,a,b,n):
	    m=Trapecios()
	    h = (b-a)/n
	    x0=a
	    area=m.funcion_evaluada(x0,funcion)+m.funcion_evaluada(b,funcion)
	    for i in range (0,int(n-1)):
	        xi=x0+h
	        area= area + 2* m.funcion_evaluada(xi,funcion)
	        x0=xi
	    rest = area * (h/2)
	    return (rest)
            
            

            
