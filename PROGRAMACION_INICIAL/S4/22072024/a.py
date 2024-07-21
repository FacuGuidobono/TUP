
UNIDAD = 1

dc    = float(input('Ingrese el tamaño de la diagonal menor CD (cm): ')) * UNIDAD

while True:
  bc_bd = float(input('Ingrese el tamaño del lado menor BC (cm): ')) * UNIDAD

  if bc_bd > dc:
      break
  else:
    print('El tamaño de BC debe ser mayor que CD. Inténtelo de nuevo.')

while True:
      da_ca = float(input('Ingrese el tamaño de los lado mayor DA (cm): ')) * UNIDAD
      if da_ca > bc_bd:
        break
      else:
        print('El tamaño de DA debe ser mayor que BC. Inténtelo de nuevo.')
    
print('SuSSEsc')