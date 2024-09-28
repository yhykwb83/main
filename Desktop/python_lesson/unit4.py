#Compare two numbers
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

result = compare(1, 2)
print(result)

#Calculate the remaining side of the triangle
import math
def radius(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print('radius is:', result)
    return result

#Calcurate the area 
def area(distance):
    area = distance ** 2 * math.pi
    print('area is:', area)
    return area

area(radius(1, 2, 4, 6))

#Compare 3 numbers

def is_between(x, y, z):
    return x<= y <= z
print(is_between(2, 5, 9))

