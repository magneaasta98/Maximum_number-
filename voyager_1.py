n = int(input('Fjöldi daga: '))
v = 38241 #miles/hr
d = 16637000000
t = n * 24
miles = v*t+d #milur frá sólinni
km = round(miles*1.609344)
AU = round(miles/92955887)

print('Miles from the sun: ',miles,'\n'
      'Kilometers from the sun: ',km,'\n'
      'AU from the sun: ',AU)

