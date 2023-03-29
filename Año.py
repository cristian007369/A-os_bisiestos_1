## PROGRAMA PARA SABER SI UN AÑO ES BISIESTO

print ("----------------------------------------------")
print ("-----------CUANDO UN AÑO ES BISIESTO----------")
print ("----------------------------------------------")

#INPUT
print("Si el año es antes de Cristo a.C. escribalo como un negativo")
año= int(input("Dígite el año: "))
mes=int(input("Ingrese el mes: "))
dia=int(input("Ingrese el día: "))

a=año%4 
b=año%100 
c=año%400 

#PROCESING
if año>=1582 and a==0 and b==0 and c==0 or año>=1582 and a==0 and b!=0 or año <1582 and año>=-46 and a==0 or año<-46:
    if mes>0 and mes<=12 and dia>0 and dia<=31:
         if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia<=31:
             rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
         elif mes==4 or mes==6 or mes==9 or mes==11 and dia<=30:
             rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
         elif mes==2 and dia<=29:
             rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
         else:
             rta="Fecha invalidad"
    else:
         rta="Fecha invalidad"
else:
    if mes>0 and mes<=12 and dia>0 and dia<=31:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia<=31 :
            rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
        elif mes==4 or mes==6 or mes==9 or mes==11 and dia<=30:
            rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
        elif mes==2 and dia<=28:
            rta="Año " + str(año) + " mes " + str(mes) +" día "+ str(dia) +" , esté año fue un año bisiesto"
        else:
            rta="Fecha invalidad"
    else:
        rta="Fecha invalidad"

#OUTPUT

print ("----------------------------------------------")
print (rta)
print ("----------------------------------------------")