
class Tdbits:

    def __init__(self):
        return

    #funcion entero-binario
    def entero_binario(self,part_e):
        bin_decimal=[0]
        i=part_e
        num1=0
        count2=0
        while i>1:
            num1=int(i%2)
            i=int(i/2)
            if count2>0:
                bin_decimal.append(num1)
            else:
                bin_decimal[count2]=num1
            count2=count2+1
        bin_decimal.append(i)
        bin_decimal.reverse()
        return bin_decimal

    #funcion fraccionario-binario
    def fraccionario_binario(self,part_f):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<25:
            i=i*2
            num1=int(i)
            i=i-num1
            if count>0:
                bin_fraccionaria.append(num1)
            else:
                bin_fraccionaria[count]=num1
            count=count+1
        return bin_fraccionaria

    def entero_binario_expo(self,expo):
        bin_decimal_expo=[0]
        i=expo
        num1=0
        count2=0
        while i>1:
            num1=int(i%2)
            i=int(i/2)
            if count2>0:
                bin_decimal_expo.append(num1)

            else:
                bin_decimal_expo[count2]=num1
            count2=count2+1
        bin_decimal_expo.append(i)
        bin_decimal_expo.reverse()
        return bin_decimal_expo


    #def paso1ConvertirBinario(part_e):


    def paso2NormalizarExpDos(self,decimal):
        TDbits_decimal=[0]
        TdExponente=[0]
        TDbits_fraccionaria =[0]
        part_e = int(decimal) #Parte entera con o sin signo
        part_f = abs(decimal) - abs(int(decimal)) #Parte decimal

        m=Tdbits()
        count=0
        if(part_e<0):
                part_e=part_e*-1

        bin_decimal=m.entero_binario(part_e)
        i=len(bin_decimal)
        #normalizo el numero
        while count<i-1:
            if count>0:
                TDbits_decimal.append(bin_decimal[count+1])
            else:
                TDbits_decimal[count]=bin_decimal[count+1]
            count=count+1
        #transformo el exponente
        expo=127+len(TDbits_decimal)
        count3=0
        mantisa=23-len(TDbits_decimal)
        # si el numero tiene parte fraccionaria
        bin_fraccionaria=m.fraccionario_binario(part_f)
        variable=0
        while mantisa>0:
            if variable>=len(bin_fraccionaria):
                TDbits_decimal.append(0)
            else:
                TDbits_decimal.append(bin_fraccionaria[variable])
            mantisa=mantisa-1
            variable=variable+1
        #paso el exponente a binario
        for x in bin_decimal[:]:
             bin_decimal.remove(x)
        bin_decimal_expo=m.entero_binario_expo(expo)
        i=len(bin_decimal_expo)

        while count3<i:
            if count3>0:
                TdExponente.append(bin_decimal_expo[count3])
            else:
                TdExponente[count3]=bin_decimal_expo[count3]
            count3=count3+1
        if decimal>0:

            posi32="0"+"-"+''.join(str(e) for e in TdExponente)+"-"+''.join(str(e) for e in TDbits_decimal)
            return posi32
        if decimal<1:
            nega32="1"+"-"+''.join(str(e) for e in TdExponente)+"-"+''.join(str(e) for e in TDbits_decimal)
            return nega32

class Scbits:

    def __init__(self):
        return
    #funcion entero-binario
    def entero_binario(self,part_e):
        bin_decimal=[0]
        i=part_e
        num1=0
        count2=0
        while i>1:
            num1=int(i%2)
            i=int(i/2)
            if count2>0:
                bin_decimal.append(num1)
            else:
                bin_decimal[count2]=num1
            count2=count2+1
        bin_decimal.append(i)
        bin_decimal.reverse()
        return bin_decimal

    #funcion fraccionario-binario
    def fraccionario_binario(self,part_f):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<25:
            i=i*2
            num1=int(i)
            i=i-num1
            if count>0:
                bin_fraccionaria.append(num1)
            else:
                bin_fraccionaria[count]=num1
            count=count+1
        return bin_fraccionaria

    def entero_binario_expo(self,expo):
        bin_decimal_expo=[0]
        i=expo
        num1=0
        count2=0
        while i>1:
            num1=int(i%2)
            i=int(i/2)
            if count2>0:
                bin_decimal_expo.append(num1)

            else:
                bin_decimal_expo[count2]=num1
            count2=count2+1
        bin_decimal_expo.append(i)
        bin_decimal_expo.reverse()
        return bin_decimal_expo


    def paso2NormalizarExpDos(self,decimal):
        TDbits_decimal=[0]
        TdExponente=[0]
        TDbits_fraccionaria =[0]
        part_e = int(decimal) #Parte entera con o sin signo
        part_f = abs(decimal) - abs(int(decimal)) #Parte decimal
        m=Scbits()
        count=0
        if(part_e<0):
                part_e=part_e*-1

        bin_decimal=m.entero_binario(part_e)
        i=len(bin_decimal)
        #normalizo el numero
        while count<i-1:
            if count>0:
                TDbits_decimal.append(bin_decimal[count+1])
            else:
                TDbits_decimal[count]=bin_decimal[count+1]
            count=count+1
        #transformo el exponente
        expo=1023+len(TDbits_decimal)
        count3=0
        mantisa=52-len(TDbits_decimal)
        bin_fraccionaria=m.fraccionario_binario(part_f)
        variable=0
        while mantisa>0:
            if variable>=len(bin_fraccionaria):
                TDbits_decimal.append(0)
            else:
                TDbits_decimal.append(bin_fraccionaria[variable])
            mantisa=mantisa-1
            variable=variable+1
        #paso el exponente a binario
        for x in bin_decimal[:]:
             bin_decimal.remove(x)
        bin_decimal_expo=m.entero_binario_expo(expo)
        i=len(bin_decimal_expo)

        while count3<i:
            if count3>0:
                TdExponente.append(bin_decimal_expo[count3])
            else:
                TdExponente[count3]=bin_decimal_expo[count3]
            count3=count3+1
        if decimal>0:
            posi64="0"+"-"+''.join(str(e) for e in TdExponente)+"-"+''.join(str(e) for e in TDbits_decimal)
            return posi64
        if decimal<1:
            nega64="0"+"-"+''.join(str(e) for e in TdExponente)+"-"+''.join(str(e) for e in TDbits_decimal)
            return nega64


#--------------------inversas

class Invtdieee:
    def __init__(self):
        return

    def fraccionario_bin_oct_hex(self,part_f):
        sumita=0
        j=1
        i=0
        eso=str(part_f)
        for x in eso:
            if(i>1):
                n=int(x)
                sumita=sumita+n*2**-j

                j=j+1
            i=i+1
        #str1 = str(sumita)
        return sumita

    def binarioToDecimal(self,binario):
         return str(int(binario,2))

    def convertirElNumerotd(self,signo,exponente,mantisa):
         m=Invtdieee()
         part_e=[0]
         part_f=[0]
         part_e[0]=1
         binario = int(exponente)
         decimal = m.binarioToDecimal(str(binario))
         parteNor=int(decimal)-127
         sacar=str(mantisa)
         cont=0
         cont2=0
         for x in sacar:
             if(cont<parteNor):
                 part_e.append(int(x))
             if(cont==parteNor):
                 part_f[cont2]="0."
             if(cont>=parteNor):
                 part_f.append(int(x))
             cont=cont+1
         str1 = ''.join(str(e) for e in part_e)
         str2 = ''.join(str(e) for e in part_f)
         binario = int(str1)
         decimal = m.binarioToDecimal(str(binario))
         fraccion=m.fraccionario_bin_oct_hex(float(str2))
         total=str(int(decimal)+float(fraccion))
         return total

class Invscieee:
    def __init__(self):
        return

    def fraccionario_bin_oct_hex(self,part_f):
        sumita=0
        j=1
        i=0
        eso=str(part_f)
        for x in eso:
            if(i>1):
                n=int(x)
                sumita=sumita+n*2**-j

                j=j+1
            i=i+1
        #str1 = str(sumita)
        return sumita

    def binarioToDecimal(self,binario):
        return str(int(binario,2))

    def convertirElNumerosc(self,signo,exponente,mantisa):
         m=Invscieee()
         part_e=[0]
         part_f=[0]
         part_e[0]=1
         binario = int(exponente)
         decimal = m.binarioToDecimal(str(binario))
         parteNor=int(decimal)-1023
         sacar=str(mantisa)
         cont=0
         cont2=0
         for x in sacar:
             if(cont<parteNor):
                 part_e.append(int(x))
             if(cont==parteNor):
                 part_f[cont2]="0."
             if(cont>=parteNor):
                 part_f.append(int(x))
             cont=cont+1
         str1 = ''.join(str(e) for e in part_e)
         str2 = ''.join(str(e) for e in part_f)
         binario = int(str1)
         decimal = m.binarioToDecimal(str(binario))
         fraccion= m.fraccionario_bin_oct_hex(float(str2))
         total=str(int(decimal)+float(fraccion))
         return total
