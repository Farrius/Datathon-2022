from py2opt.routefinder import RouteFinder

names = []
x = []
y = []

def readFile(fileName):
	with open(fileName, "rt") as myFile:
		for line in myFile:
			if (line[0] == '-'):
				ar = line.split(' ');
				driver_name = ar[1]
				driver_type = ar[7]
				line = next(myFile)
				line = next(myFile)
				ar = line.split(' ')
				#x = ar[5]
				#y = ar[6]
			elif (line[0] == 'i'):
				ar = line.split(' ')
				names.append(ar[0])
				x.append(int(ar[5]));
				y.append(int(ar[6]));

def manhattanDistance(i, j):
	return abs(x[i] - x[j]) + abs(y[i] - y[j])

readFile("testcase0.def") #Abrir fichero

dist_mat = [] #Crear la matriz para el opt2 optimization
for i in range(len(names)):
	ar = []
	for j in range(len(names)):
		ar.append(manhattanDistance(i, j));
	dist_mat.append(ar)

route_finder = RouteFinder(dist_mat, names, iterations=5)
best_distance, best_route = route_finder.solve()

print(best_distance)
#print(best_route)







