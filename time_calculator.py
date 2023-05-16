def add_time(start, duration, day=False):
  corte = start.split()
  hstart = corte[0]
  ampm = corte[1] #AM o PM
  corte2 = hstart.split(":")
  hora = int(corte2[0]) #HORAS
  minutos = int(corte2[1]) #MINUTOS

  corte3 = duration.split(":")
  hora2 = int(corte3[0])
  minutos2 = int(corte3[1])
  dias=0
  dias2=0
  if(day):
    dias=0
    day=day.capitalize()
    diastring=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if day in diastring:
      diai = diastring.index(day)
      diai+=1

  
  #FORMATO A 24HS PARA CALCULAR
  if "P" in ampm:
    hora+=12
  #CALCULO DE TIEMPO
  minutos+=minutos2
  if(minutos>60):
    resto = minutos%60
    hora+=1
    minutos = resto
  if(minutos<10):
    minutos = "0"+str(minutos)
  
  hora+=hora2
  if(hora>24):
    dias = int(hora/24)
    resto = hora%24
    hora = resto
  
  if (dias==1):
    dias2=dias
    dias=str("(next day)")
  elif (dias>1):
    dias2=dias
    dias=str("("+str(dias)+" days later)")

  if(day and diai>0):
    diai+=dias2
    if(diai<=7):
      dianuevo=diastring[diai-1]
    else:
      resto = diai%7
      dianuevo = diastring[resto-1]

  #---------- VUELVE A FORMATO DE 12HS ACLARANDO AM O PM
  if(hora>11):
    hora-=12
    ampm="PM"
    if(hora==0):
      hora=12
  else:
    ampm="AM"
    if(hora==0):
      hora=12
  
  if(day==False):
    if(dias==0):
      new_time = str(hora)+":"+str(minutos)+" "+ampm
    else:
      new_time = str(hora)+":"+str(minutos)+" "+ampm+" "+dias
  else:
    if(dias==0):
      new_time = str(hora)+":"+str(minutos)+" "+ampm+", "+day
    else:
      new_time = str(hora)+":"+str(minutos)+" "+ampm+", "+dianuevo+" "+dias

  
  
  return new_time
  
  