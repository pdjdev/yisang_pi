cap=['길은막다른골목이적당하오.',
    '다른사정은없는것이차라리나았소',
    '길은뚫린골목이라도적당하오.']
child=13

print(str(child)+'인의아해가도로로질주하오.')
print('('+cap[0]+')\n')

for c in range(child):
	print('제'+str(c+1)+'의아해',end='')
	if c>0:print('도',end='')
	else:print('가',end='')
	print('무섭다고그리오.')
print(str(child)+'인의아해는무서운아해와무서워하는아해와그렇게뿐이모였소.('+cap[1]+')\n')

for c in range(4):
	print('그중에',end='')
	if c<2:print(str(c+1)+'인의아해가무서운',end='')
	else:print(str(4-c)+'인의아해가무서워하는',end='')
	print('아해라도좋소.')
    
print('\n('+cap[2]+')')
print(str(child)+'인의아해가도로로질주하지아니하여도좋소.')
