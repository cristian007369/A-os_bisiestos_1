## PROGRAMA PARA SABER SI UN AÑO ES BISIESTO

print ("----------------------------------------------")
print ("-----------CUANDO UN AÑO ES BISIESTO----------")
print ("----------------------------------------------")

#INPUT
print("Si el año es antes de Cristo a.C. escribalo como un negativo")
año= int(input("Dígite el año: "))

a=año%4 
b=año%100 
c=año%400 

#PROCESING

if año>=1582 and a==0 and b==0 and c==0:
    rta="El año es bisiesto"
elif año>=1582 and a==0 and b!=0:
    rta="El año es bisiesto"
elif año <1582 and año>=-46 and a==0:
    rta="El año es bisiesto"
elif año<-46:
    rta="En esta epoca no existian los años bisiestos"
else:
    rta="El año no es bisiesto"

#OUTPUT

print ("----------------------------------------------")
print (rta)
print ("----------------------------------------------")