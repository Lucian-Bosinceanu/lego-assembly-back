import random

# random(2) is for 0 (to increment negative value of x/z) and 1 (to increment pozitive value of x/z)
# 0 is for 'x' coordinate
# 1 is for 'y' coordinate
# 2 is for 'z' coordinate
# timer represent how many time a can receive 1 from random and still stay at that level

def create_random_JSON_file(number_of_cubes, timer):
    x_number_pozitive = 0
    x_number_negative = 0
    z_number_pozitive = 0
    z_number_negative = 0
    y_number_pozitive = 0
    timer_aux = 0
    i = 1

    # code for first element of array 
    f = open("myfile.json", "w")
    f.write('{\n"cubes":[\n')
    f.write('{\n')
    f.write('"x":0,\n')
    f.write('"y":0,\n')
    f.write('"z":0,\n')
    f.write('"color":null\n')
    f.write('}\n')
    nr_cubes = 1

    while(i < number_of_cubes):
        if(random.randrange(3) == 1): # for 'y' coordinate
            timer_aux = timer_aux + 1
            if(timer_aux == timer):
                y_number_pozitive = y_number_pozitive + 1
                timer_aux = 0
                x_number_pozitive = 0
                x_number_negative = 0
                z_number_pozitive = 0
                z_number_negative = 0
                      
                f.write(',\n')
                # code to write in json
                f.write('{\n')
                f.write('"x":')
                f.write('{}'.format(x_number_pozitive))
                f.write(',\n')
                f.write('"y":')
                f.write('{}'.format(y_number_pozitive))
                f.write(',\n')
                f.write('"z":')
                f.write('{}'.format(z_number_pozitive))
                f.write(',\n')
                f.write('"color":null\n')
                f.write('}\n')
                nr_cubes = nr_cubes + 1

        elif(random.randrange(3) == 0): #for 'x' coordinate
            if(random.randrange(2) == 0): # the cube will be added at - x
                x_number_negative = x_number_negative + 1
                
                # code to write in json
                f.write(',\n')
                f.write('{\n')
                f.write('"x":')
                f.write('{}'.format(x_number_negative * (-1)))
                f.write(',\n')
                f.write('"y":')
                f.write('{}'.format(y_number_pozitive))
                f.write(',\n')
                f.write('"z":')
                f.write('{}'.format(random.randrange(z_number_negative + 1) * (-1)))
                f.write(',\n')
                f.write('"color":null\n')
                f.write('}\n')
                nr_cubes = nr_cubes + 1

            elif(random.randrange(2) == 1): # the cube will be added at + x
                x_number_pozitive = x_number_pozitive + 1

                # code to write in json
                f.write(',\n')
                f.write('{\n')
                f.write('"x":')
                f.write('{}'.format(x_number_pozitive))
                f.write(',\n')
                f.write('"y":')
                f.write('{}'.format(y_number_pozitive))
                f.write(',\n')
                f.write('"z":')
                f.write('{}'.format(random.randrange(z_number_pozitive + 1)))
                f.write(',\n')
                f.write('"color":null\n')
                f.write('}\n')
                nr_cubes = nr_cubes + 1

        elif(random.randrange(3) == 2): #for 'z' coordinate
            if(random.randrange(2) == 0): # the cube will be added at - z
                z_number_negative = z_number_negative + 1

                # code to write in json
                f.write(',\n')
                f.write('{\n')
                f.write('"x":')
                f.write('{}'.format(random.randrange(x_number_negative + 1) * (-1)))
                f.write(',\n')
                f.write('"y":')
                f.write('{}'.format(y_number_pozitive))
                f.write(',\n')
                f.write('"z":')
                f.write('{}'.format(z_number_negative * (-1)))
                f.write(',\n')
                f.write('"color":null\n')
                f.write('}\n')
                nr_cubes = nr_cubes + 1

            elif(random.randrange(2) == 1): # the cube will be added at + z
                z_number_pozitive = z_number_pozitive + 1

                # code to write in json
                f.write(',\n')
                f.write('{\n')
                f.write('"x":')
                f.write('{}'.format(random.randrange(x_number_pozitive + 1)))
                f.write(',\n')
                f.write('"y":')
                f.write('{}'.format(y_number_pozitive))
                f.write(',\n')
                f.write('"z":')
                f.write('{}'.format(z_number_pozitive + 1))
                f.write(',\n')
                f.write('"color":null\n')
                f.write('}\n')
                nr_cubes = nr_cubes + 1

        i = i + 1
    print(nr_cubes)
    f.write(']\n}\n')
    f.close()


create_random_JSON_file(7000, 100)

