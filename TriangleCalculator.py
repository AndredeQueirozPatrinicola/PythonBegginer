import math

side_1 = float(input('Put the size of one side of your triangle: '))
side_2 = float(input('Another side: '))
side_3 = float(input('And another one: '))

ang_1 = float(input('Now put the angle of the first side with the second: '))
ang_2 = float(input('Side 2 with side 3: '))
ang_3 = float(input('Side 3 with side 1: '))

a = side_1
b = side_2
c = side_3
d = ang_1
e = ang_2
f = ang_3

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("It's an equilateral triangle")
    elif a == b or b == c or a == c:
        print("It's an isoceles triangle")
    elif a != b != c:
        print("It's a scalene triangle")
else:
    print("It's not a triangle")
   

if d + e + f == 180:
    if d < 90 and e < 90 and f < 90:
        print("It's an acute triangle")
        herons = (a + b + c) / 2 
        h = herons
        area = math.sqrt(h*(h - a)*(h - b)*(h - c))
        area_format = "{:.2f}".format(area)
        print("The area is:", area_format)
    if d == 90 or e == 90 or f == 90:
        print("It's a right triangle")
        if a != b != c:
            r_values = [a, b, c]
            r_values.sort()
            base = r_values[0]
            height = r_values[1]
            area = (base * height) / 2
            print("The area is:", area)
        elif a == b or b == c or a == c:
            ri_values = [a, b, c]
            ri_values.sort()
            base = ri_values[0]
            height = ri_values[1]
            area = (base * height) / 2
            print("The area is:", area)
        else:
            print("Not a valid triangle")
    if d > 90 or e > 90 or f > 90:
        print("It's an obtuse triangle")
        herons = (a + b + c) / 2 
        h = herons
        area = math.sqrt(h*(h - a)*(h - b)*(h - c))
        area_format = "{:.2f}".format(area)
        print("The area is:", area_format)
else:
    print("Angles not compatible with a triangle.")
