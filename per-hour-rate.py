a=float(input('what\'s your rate/hour'))
b=float(input('how many hours do you work per day'))
c=float(input('do you get any extra bonus'))
t=float(a*b)
print('today monthly income is',t*30,'per day income',t,'excluding bonus of \n',c,)
print('total gross income is',t*30+c)
