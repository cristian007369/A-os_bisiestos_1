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

if año>=-46:
    if año>=1582:
        if a==0:
             if b==0:
                 if c==0:
                     rta="El año es bisiesto"
                 else: 
                     rta="El año no es bisiesto"
             else:
                 rta="El año es bisiesto"
        else:
             rta="El año no es bisiesto"
    else: 
        if a==0:
            rta="El año es bisiesto"
        else:
            rta="El año no es bisiesto"
else:
    rta="En este año no existian los años bisiestos"

#OUTPUT

print ("----------------------------------------------")
print (rta)
print ("----------------------------------------------")
