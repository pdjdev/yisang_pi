print('환자의용태에관한문제.')
for i in range(10,-1,-1):
	print()
	for j in range(10,0,-1):
		if i==j:print('.',end=' ')
		print(j%10,end=' ')
print('.\n\n진단 0:1\n  26.10.1931\n    이상 책임의사 이 상')
