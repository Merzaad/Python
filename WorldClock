import datetime
now=datetime.datetime.now()
print(now)
while 1<2:
    hr=now.hour
    mn=now.minute
    ct=input('City? ')
    if str(ct).lower()=='london':
      hr=hr-4
      if mn<30:
          mn=mn+30
      else:
          mn=mn-30
      print(str(hr),':',str(mn))
      break
    elif  str(ct).lower()=='exit':
      break
    else:
      print(ct,'does not added')
