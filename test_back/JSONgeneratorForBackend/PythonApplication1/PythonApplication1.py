def create_json(count):
	f = open("myfile", "w")
	f.write('{\n"cubes":[\n')
	f.write('{\n')
	f.write('"x":0,\n')
	f.write('"y":0,\n')
	f.write('"z":0,\n')
	f.write('"color":null\n')
	f.write('}\n')

	i = 1
	while(i < count):
		f.write(',\n')
		f.write('{\n')
		f.write('"x":')
		f.write('{}'.format(i))
		f.write(',\n')
		f.write('"y":0,\n')
		f.write('"z":0,\n')
		f.write('"color":null\n')
		f.write('}\n')
		i = i + 1

	f.write(']\n}\n')
	f.close()

create_json(5001)


print("merge")