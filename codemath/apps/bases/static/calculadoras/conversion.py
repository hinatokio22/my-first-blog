class Decimalotras:

    def __init__(self):
        return

    def decimalToBinario(self,decimal):
        return bin(int(decimal))

    def decimalToOctal(self,decimal):
        return oct(int(decimal))

    def decimalToHexadecimal(self,decimal):
        return hex(int(decimal))


    def decimalToOthers(self,decimal):
         m=Decimalotras()
         #decimal = pedirValor("decimal")
         part_e = int(decimal) #Parte entera con o sin signo
         part_f =( abs(decimal) - abs(int(decimal)) )#Parte decimal
         basediv=2
         decimalotras=[0]

         binario = m.decimalToBinario(part_e)
         fraccion= m.fraccionario_decimal(part_f,basediv)
         if(float(fraccion)==0):
             total=str(binario)
             decimalbin=str(total)
         else:
             decimalbin=str(binario+","+fraccion)

         basediv=8
         octal = m.decimalToOctal(decimal)
         fraccion= m.fraccionario_decimal(part_f,basediv)
         decimalotras.append(str(octal+","+fraccion))
         if(float(fraccion)==0):
             total=str(octal)
             decimalbin=str(decimalbin+"-"+total)
         else:
             decimalbin=str(decimalbin+"-"+octal+","+fraccion)
         #decimalbin=str(octal+","+fraccion)

         basediv=16
         hexadecimal = m.decimalToHexadecimal(decimal)
         fraccion= m.fraccionario_decimal(part_f,basediv)
         decimalotras.append(str(hexadecimal+","+fraccion))
         decimalbin=str(decimalbin+"-"+hexadecimal+","+fraccion)
         #decimalbin=str(hexadecimal+","+fraccion)

         return (decimalbin)

    def fraccionario_decimal(self,part_f,basediv):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<24:
            i=i*basediv
            num1=int(i)
            i=i-num1
            if(basediv<10):
                if count>0:
                    bin_fraccionaria.append(num1)
                else:
                    bin_fraccionaria[count]=num1
                count=count+1
            else:
                if count==0:
                    if num1<10:
                        bin_fraccionaria[count]=num1
                    else:
                        if num1==10:
                            bin_fraccionaria[count]=("A")
                        if num1==11:
                            bin_fraccionaria[count]=("B")
                        if num1==12:
                            bin_fraccionaria[count]=("C")
                        if num1==13:
                            bin_fraccionaria[count]=("D")
                        if num1==14:
                            bin_fraccionaria[count]=("E")
                        if num1==15:
                            bin_fraccionaria[count]=("F")

                if count>0:
                    if num1<10:
                        bin_fraccionaria.append(num1)
                    else:
                        if num1==10:
                            bin_fraccionaria.append("A")
                        if num1==11:
                            bin_fraccionaria.append("B")
                        if num1==12:
                            bin_fraccionaria.append("C")
                        if num1==13:
                            bin_fraccionaria.append("D")
                        if num1==14:
                            bin_fraccionaria.append("E")
                        if num1==15:
                            bin_fraccionaria.append("F")
                count=count+1

        str1 = ''.join(str(e) for e in bin_fraccionaria)
        bin_fraccionaria=bin_fraccionaria[0]
        return str1

class Binariootras:

    def __init__(self):
        return

    def decimalToOctal(self,decimal):
        return oct(int(decimal))

    def decimalToHexadecimal(self,decimal):
        return hex(int(decimal))

    def binarioToDecimal(self,binario):
        return str(int(binario,2))

    def binarioToOctal(self,binario):
        m=Binariootras()
        decimal = m.binarioToDecimal(binario)
        return m.decimalToOctal(decimal)

    def binarioToHexadecimal(self,binario):
        m=Binariootras()
        decimal = m.binarioToDecimal(binario)
        return m.decimalToHexadecimal(decimal)

    def fraccionario_bin_oct(self,part_f,basediv):
        sumita=0
        j=1
        i=0
        eso=str(part_f)
        for x in eso:
            if(i>1):
                n=int(x)
                sumita=sumita+n*basediv**-j

                j=j+1
            i=i+1
        return sumita

    def binarioToOthers(self,binario):
         binariootras=[0]
         m=Binariootras()
         part_e = int(binario) #Parte entera con o sin signo
         part_f =( abs(binario) - abs(int(binario)) )#Parte decimal
         basedivcom=2
         tamano=0
         cont=str(part_e)
         sumi=0
         for x in cont:
             sumi=sumi+1
         contar=str(binario)
         con=0
         for x in contar:
             if(x=="1" or x=="0" or x=="."):

                 if(con>sumi-2):
                     tamano=tamano+1
                 con=con+1
         epa=round(part_f,tamano-2)
         decimal = m.binarioToDecimal(str(part_e))
         fraccion= m.fraccionario_bin_oct(epa,basedivcom)
         #binariootras[0]=str(int(decimal)+float(fraccion))
         if(float(fraccion)==0):
             total=str(decimal)
             binotras=str(total)
         else:
             binotras=str(int(decimal)+float(fraccion))

         basediv=8
         octal = m.binarioToOctal(str(part_e))
         frac_des=m.fraccionario_bin_oct(epa,basedivcom)
         fraccion=m.fraccionario_decimal(frac_des,basediv)
         #binariootras.append(str(str(octal)+","+fraccion))
         if(float(fraccion)==0):
             total=str(octal)
             binotras=str(binotras+"-"+total)
         else:
             binotras=str(binotras+"-"+octal+","+fraccion)

         basediv=16
         hexadecimal = m.binarioToHexadecimal(str(part_e))
         frac_des=m.fraccionario_bin_oct(epa,basedivcom)
         fraccion=m.fraccionario_decimal(frac_des,basediv)
         #binariootras.append(str(str(hexadecimal)+","+fraccion))
         binotras=str(binotras+"-"+hexadecimal+","+fraccion)
         return (binotras)

    def fraccionario_decimal(self,part_f,basediv):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<24:
            i=i*basediv
            num1=int(i)
            i=i-num1
            if(basediv<10):
                if count>0:
                    bin_fraccionaria.append(num1)
                else:
                    bin_fraccionaria[count]=num1
                count=count+1
            else:
                if count==0:
                    if num1<10:
                        bin_fraccionaria[count]=num1
                    else:
                        if num1==10:
                            bin_fraccionaria[count]=("A")
                        if num1==11:
                            bin_fraccionaria[count]=("B")
                        if num1==12:
                            bin_fraccionaria[count]=("C")
                        if num1==13:
                            bin_fraccionaria[count]=("D")
                        if num1==14:
                            bin_fraccionaria[count]=("E")
                        if num1==15:
                            bin_fraccionaria[count]=("F")

                if count>0:
                    if num1<10:
                        bin_fraccionaria.append(num1)
                    else:
                        if num1==10:
                            bin_fraccionaria.append("A")
                        if num1==11:
                            bin_fraccionaria.append("B")
                        if num1==12:
                            bin_fraccionaria.append("C")
                        if num1==13:
                            bin_fraccionaria.append("D")
                        if num1==14:
                            bin_fraccionaria.append("E")
                        if num1==15:
                            bin_fraccionaria.append("F")
                count=count+1

        str1 = ''.join(str(e) for e in bin_fraccionaria)
        bin_fraccionaria=bin_fraccionaria[0]
        return str1


class Octalotras:

    def __init__(self):
        return

    def OctalToDecimal(self,octal):
        return str(int(octal, 8))

    def OctalToBinario(self,octal):
        return bin(int(str(int(octal, 8))))

    def OctalToHexadecimal(self,octal):
        return hex(int(str(int(octal, 8))))

    def fraccionario_bin_oct(self,part_f,basediv):
        sumita=0
        j=1
        i=0
        eso=str(part_f)
        for x in eso:
            if(i>1):
                n=int(x)
                sumita=sumita+n*basediv**-j

                j=j+1
            i=i+1
        return sumita

    def octalToOthers(self,octal):
         octalotras=[0]
         m=Octalotras()
         part_e = int(octal) #Parte entera con o sin signo
         part_f =( abs(octal) - abs(int(octal)) )#Parte decimal

         basedivcom=8
         decimal = m.OctalToDecimal(str(part_e))
         fraccion= m.fraccionario_bin_oct(part_f,basedivcom)
         #octalotras[0]=str(int(decimal)+float(fraccion))
         if(float(fraccion)==0):
             total=str(decimal)
             octalbin=str(total)
         else:
             octalbin=str(int(decimal)+float(fraccion))

         basediv=2
         binario = m.OctalToBinario(str(part_e))
         frac_des= m.fraccionario_bin_oct(part_f,basedivcom)
         fraccion= m.fraccionario_decimal(frac_des,basediv)
         #octalotras.append(str(str(binario)+","+fraccion))
         if(float(fraccion)==0):
             total=str(binario)
             octalbin=str(octalbin+"-"+total)
         else:
             octalbin=str(octalbin+"-"+binario+","+fraccion)

         basediv=16
         hexadecimal = m.OctalToHexadecimal(str(part_e))
         frac_des= m.fraccionario_bin_oct(part_f,basedivcom)
         fraccion= m.fraccionario_decimal(frac_des,basediv)
         #octalotras.append(str(str(hexadecimal)+","+fraccion))
         octalbin=str(octalbin+"-"+hexadecimal+","+fraccion)
         return (octalbin)

    def fraccionario_decimal(self,part_f,basediv):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<24:
            i=i*basediv
            num1=int(i)
            i=i-num1
            if(basediv<10):
                if count>0:
                    bin_fraccionaria.append(num1)
                else:
                    bin_fraccionaria[count]=num1
                count=count+1
            else:
                if count==0:
                    if num1<10:
                        bin_fraccionaria[count]=num1
                    else:
                        if num1==10:
                            bin_fraccionaria[count]=("A")
                        if num1==11:
                            bin_fraccionaria[count]=("B")
                        if num1==12:
                            bin_fraccionaria[count]=("C")
                        if num1==13:
                            bin_fraccionaria[count]=("D")
                        if num1==14:
                            bin_fraccionaria[count]=("E")
                        if num1==15:
                            bin_fraccionaria[count]=("F")

                if count>0:
                    if num1<10:
                        bin_fraccionaria.append(num1)
                    else:
                        if num1==10:
                            bin_fraccionaria.append("A")
                        if num1==11:
                            bin_fraccionaria.append("B")
                        if num1==12:
                            bin_fraccionaria.append("C")
                        if num1==13:
                            bin_fraccionaria.append("D")
                        if num1==14:
                            bin_fraccionaria.append("E")
                        if num1==15:
                            bin_fraccionaria.append("F")
                count=count+1

        str1 = ''.join(str(e) for e in bin_fraccionaria)
        bin_fraccionaria=bin_fraccionaria[0]
        return str1



class Hexadecimalotras:


    def __init__(self):
        return

    def HexadecimalToDecimal(self,hexadecimal):
        return  str(int(hexadecimal,16))

    def HexadecimalToBinario(self,hexadecimal):
        return bin(int(hexadecimal, 16))

    def HexadecimalToOctal(self,hexadecimal):
        return oct(int(hexadecimal,16))

    def fraccionario_hex(self,part_f,basediv):
        sumita=0
        j=1
        i=0
        eso=str(part_f)
        for x in eso:
            if(i>1):
                if(x=="a" or x=="A"):
                    x=10
                if(x=="b" or x=="B"):
                    x=11
                if(x=="c" or x=="C"):
                    x=12
                if(x=="d" or x=="D"):
                    x=13
                if(x=="e" or x=="E"):
                    x=14
                if(x=="f" or x=="F"):
                    x=15
                n=int(x)
                sumita=sumita+n*basediv**-j

                j=j+1
            i=i+1
        return sumita

    def hexadecimalToOthers(self,completo):
         #hexadeciotros=[0]
         m=Hexadecimalotras()
         sumi=0
         hexadecimal=""
         part_f=""
         spliteado = completo.split('.')
         hexadecimal=spliteado[0]
         if(len(spliteado)>1):     
             part_f=spliteado[1]

         basedivcom=16;
         decimal = m.HexadecimalToDecimal(hexadecimal)
         fraccion= m.fraccionario_hex(part_f,basedivcom)
         #hexadeciotros=str(int(decimal)+float(fraccion))
         if(float(fraccion)==0):
             total=str(decimal)
             hexabin=str(total)
         else:
             hexabin=str(int(decimal)+float(fraccion))

         basediv=2
         binario = m.HexadecimalToBinario(hexadecimal)
         frac_des= m.fraccionario_hex(part_f,basedivcom)
         fraccion= m.fraccionario_decimal(frac_des,basediv)
         #hexadeciotros.append(str(str(binario)+","+fraccion))
         if(float(fraccion)==0):
             total=str(binario)
             hexabin=str(hexabin+"-"+total)
         else:
             hexabin=str(hexabin+"-"+binario+","+fraccion)

         basediv=8
         octal = m.HexadecimalToOctal(hexadecimal)
         frac_des= m.fraccionario_hex(part_f,basedivcom)
         fraccion= m.fraccionario_decimal(frac_des,basediv)
         #hexadeciotros.append(str(str(octal)+","+fraccion))
         if(float(fraccion)==0):
             total=str(octal)
             hexabin=str(hexabin+"-"+total)
         else:
             hexabin=str(hexabin+"-"+octal+","+fraccion)
         return (hexabin)

    def fraccionario_decimal(self,part_f,basediv):
        bin_fraccionaria =[0]
        i=part_f
        count=0
        num1=0
        while count<24:
            i=i*basediv
            num1=int(i)
            i=i-num1
            if(basediv<10):
                if count>0:
                    bin_fraccionaria.append(num1)
                else:
                    bin_fraccionaria[count]=num1
                count=count+1
            else:
                if count==0:
                    if num1<10:
                        bin_fraccionaria[count]=num1
                    else:
                        if num1==10:
                            bin_fraccionaria[count]=("A")
                        if num1==11:
                            bin_fraccionaria[count]=("B")
                        if num1==12:
                            bin_fraccionaria[count]=("C")
                        if num1==13:
                            bin_fraccionaria[count]=("D")
                        if num1==14:
                            bin_fraccionaria[count]=("E")
                        if num1==15:
                            bin_fraccionaria[count]=("F")

                if count>0:
                    if num1<10:
                        bin_fraccionaria.append(num1)
                    else:
                        if num1==10:
                            bin_fraccionaria.append("A")
                        if num1==11:
                            bin_fraccionaria.append("B")
                        if num1==12:
                            bin_fraccionaria.append("C")
                        if num1==13:
                            bin_fraccionaria.append("D")
                        if num1==14:
                            bin_fraccionaria.append("E")
                        if num1==15:
                            bin_fraccionaria.append("F")
                count=count+1

        str1 = ''.join(str(e) for e in bin_fraccionaria)
        bin_fraccionaria=bin_fraccionaria[0]
        return str1
