
def add3dicts(d1,d2,d3):
	dic3 = lambda x,y,z: tuple(set({x,y,z}))
	dic2 = lambda x,y: tuple(set({x,y}))
	dic1 = lambda x: x
	
	D = {}
	for i in d1.keys():
		if i in d2 and i in d3:
			D[i] = dic3(d1[i],d2[i],d3[i])
			d2.pop(i, None)
			d3.pop(i, None)
		elif i in d2: 
			D[i] = dic2(d1[i],d2[i])
			d2.pop(i, None)
		elif i in d3:
			D[i] = dic2(d1[i],d3[i])
			d3.pop(i, None)
		else:
			D[i] = dic1(d1[i])
			
	for i in d2.keys():
		if i in d3:
			D[i] = dic2(d2[i],d3[i])
			d3.pop(i, None)
		else:
			D[i] = dic1(d2[i])
			
	for i in d3.keys():
			D[i] = dic1(d3[i])
	return D
    
   
def mainEx8():
	d1 = input('> ')
	d2 = input('> ')
	d3 = input('> ')
	print(add3dicts(d1,d2,d3))
