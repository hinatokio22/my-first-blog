from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.bases.static.calculadoras.conversion import *
from apps.bases.static.calculadoras.ieee import *
from apps.bases.static.calculadoras.prueba import prueba
from apps.bases.static.calculadoras.bisreg import *
from apps.bases.static.calculadoras.trapecios import *
from apps.bases.static.calculadoras.rectangulos import *
from apps.bases.static.calculadoras.bisreg import *

from math import*
#from sympy import diff
#from sympy.solvers import solve
def Bases(request):
    if (request.method=='POST'):
        decimal=request.POST['decimal']
        binaria=request.POST['binario']
        octall=request.POST['octal']
        hexadeci=request.POST['hexadecimal']
        if(decimal !=""):
            mostrar=Decimalotras()
            enviar=mostrar.decimalToOthers(float(decimal))
            todos=enviar.split("-")
            bina=todos[0]
            octa=todos[1]
            hexa=todos[2]
            most="epaaa"
            return render(request,'blog/convertir.html',{"bina":bina,"octa":octa,"hexa":hexa} )
        if(binaria !=""):
            mostrar=Binariootras()
            enviar=mostrar.binarioToOthers(float(binaria))
            todos=enviar.split("-")
            deci=todos[0]
            octa=todos[1]
            hexa=todos[2]
            most="epaaa"
            return render(request,'blog/convertir.html',{"deci":deci,"octa":octa,"hexa":hexa} )
        if(octall !=""):
            mostrar=Octalotras()
            enviar=mostrar.octalToOthers(float(octall))
            todos=enviar.split("-")
            deci=todos[0]
            bina=todos[1]
            hexa=todos[2]
            most="epaaa"
            return render(request,'blog/convertir.html',{"bina":bina,"deci":deci,"hexa":hexa} )
        if(hexadeci !=""):
            mostrar=Hexadecimalotras()
            enviar=mostrar.hexadecimalToOthers(str(hexadeci))
            todos=enviar.split("-")
            deci=todos[0]
            bina=todos[1]
            octa=todos[2]
            most="epaaa"
            return render(request,'blog/convertir.html',{"bina":bina,"octa":octa,"deci":deci} )
    else:
        bina=""
        octa=""
        hexa=""
        mostra=prueba()
    return render(request,'blog/convertir.html',{"bina":bina,"octa":octa,"hexa":hexa} )

def Ieeetd(request):
    if (request.method=='POST'):
        funcion=request.POST['decimal']
        signo=request.POST['signo']
        expon=request.POST['expon']
        mantisa=request.POST['mantisa']
        if(funcion!=""):
            mostrar=Tdbits()
            enviar=mostrar.paso2NormalizarExpDos(float(funcion))
            todos=enviar.split("-")
            sign=todos[0]
            exponen=todos[1]
            mantis=todos[2]
            return render(request,'blog/32bits.html',{"sign":sign,"exponen":exponen,"mantis":mantis} )
        if(signo!="" and expon!="" and mantisa!=""):
            mostrar=Invtdieee()
            enviar=mostrar.convertirElNumerotd(signo,expon,mantisa)
            return render(request,'blog/32bits.html',{"dec":enviar} )
    else:
        sign=""
        mostra=prueba()
    return render(request,'blog/32bits.html',{"sign":sign} )

def Ieeesc(request):
    if (request.method=='POST'):
        funcion=request.POST['decimal']
        signo=request.POST['signo']
        expon=request.POST['expon']
        mantisa=request.POST['mantisa']
        if(funcion!=""):
            mostrar=Scbits()
            enviar=mostrar.paso2NormalizarExpDos(float(funcion))
            todos=enviar.split("-")
            sign=todos[0]
            exponen=todos[1]
            mantis=todos[2]
            return render(request,'blog/64bits.html',{"sign":sign,"exponen":exponen,"mantis":mantis} )
        if(signo!="" and expon!="" and mantisa!=""):
            mostrar=Invscieee()
            enviar=mostrar.convertirElNumerosc(signo,expon,mantisa)
            return render(request,'blog/64bits.html',{"dec":enviar} )
    else:
        sign=""
        mostra=prueba()
    return render(request,'blog/64bits.html',{"sign":sign} )

#def Limpiar():
#    return

def Menuieee(request):
    return render(request,'blog/convermenu.html',{} )

def Biseccion(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Bisec()
        enviar=mostrar.biseccionraiz(funcion,float(a),float(b),float(error))
        return render(request,'blog/biseccion.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/biseccion.html',{"enviar":enviar} )

def Reglafalsa(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Regla_falsa()
        enviar=mostrar.regla_falsaraiz(funcion,float(a),float(b),float(error))
        return render(request,'blog/reglafalsa.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/reglafalsa.html',{"enviar":enviar} )

def Newton(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        #mostrar=Regla_falsa()
        #enviar=mostrar.regla_falsaraiz(funcion,float(a),float(b),float(error))
        return render(request,'blog/newton.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/newton.html',{"enviar":enviar} )

def Secante(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Secantec()
        enviar=mostrar.secantef(funcion,float(a),float(b),float(error))
        return render(request,'blog/secante.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/secante.html',{"enviar":enviar} )

def Polinomios(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        mostrar=Polin()
        enviar=mostrar.raizPolinomios(funcion)
        return render(request,'blog/polinomios.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/polinomios.html',{"enviar":enviar} )


def Evaluador(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        x=request.POST['valorx']
        mostra=Evalu()
        enviar=mostra.evalua(float(x),funcion)
        return render(request,'blog/evaluador.html',{"enviar":enviar} )
    else:
        enviar="nada"
        mostra=prueba()
    return render(request,'blog/evaluador.html',{"enviar":enviar} )

"""
def Bits32(request):
    if (request.method=='POST'):
        nuevo=request.POST['funcion']
        otro=request.POST['intervaloa']
        mostra=prueba()
        enviar=mostra.probando(otro,nuevo)
        return render(request,'blog/32bits.html',{"enviar":enviar} )
    else:
        enviar="nada"
        mostra=prueba()
    return render(request,'blog/32bits.html',{"enviar":enviar} )

def Bits64(request):
    if (request.method=='POST'):
        nuevo=request.POST['funcion']
        otro=request.POST['intervaloa']
        mostra=prueba()
        enviar=mostra.probando(otro,nuevo)
        return render(request,'blog/64bits.html',{"enviar":enviar} )
    else:
        enviar="nada"
        mostra=prueba()
    return render(request,'blog/64bits.html',{"enviar":enviar} )
"""
def Simpson13(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Simp13()
        enviar=mostrar.simpin13(int(particiones),float(a),float(b),funcion)
        return render(request,'blog/simpson13.html',{"enviar":enviar} )
    else:
        enviar=""
        mostra=prueba()
    return render(request,'blog/simpson13.html',{"enviar":enviar} )


def Trape(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Trapecios()
        enviar=mostrar.trap(funcion,float(a),float(b),int(particiones))
        return render(request,'blog/trapecios.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'blog/trapecios.html',{"enviar":enviar} )



def Rect(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Rectangulos()
        enviarIz=mostrar.recIzquierda(funcion,float(a),float(b),int(particiones))
        enviarDe=mostrar.recDerecha(funcion,float(a),float(b),int(particiones))
        enviarMe=mostrar.recMedios(funcion,float(a),float(b),int(particiones))
        return render(request,'blog/rectangulos.html',{"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe} )
    else:
        enviarIz=""
        enviarDe=""
        enviarMe=""
    return render(request,'blog/rectangulos.html',{"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe} )




def derivada(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        x=request.POST['valorx']
        mostra=Deriv()
        enviar=mostra.derivando(float(x),funcion)
        todos=enviar.split("-")
        primera=todos[0]
        primeraNum=todos[1]
        segunda=todos[2]
        segundaNum=todos[3]
        return render(request,'blog/derivada.html',{"primera":primera,"primeraNum":primeraNum,"segunda":segunda,"segundaNum":segundaNum} )
    else:
        primera=""
        primeraNum=""
        segunda=""
        segundaNum=""
    return render(request,'blog/derivada.html',{"primera":primera,"primeraNum":primeraNum,"segunda":segunda,"segundaNum":segundaNum} )
