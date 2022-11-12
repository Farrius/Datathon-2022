leer_driver = -1 # 0 -> input | 1 -> output
driver_name = ""

with open("testcase0.def", "rt") as myFile:
	for line in myFile:
		if (line[0] == '-'):
			ar = line.split(' ');
			driver_name = ar[1]
			driver_type = ar[7]
			print(driver_name, driver_type)
			line = next(myFile)
			line = next(myFile)
			ar = line.split(' ')
			x = ar[5]
			y = ar[6]
		elif (line[0] == 'i'):
			ar = line.split(' ')
			name = ar[0] + ar[1]
			x = ar[5]
			y = ar[6]
