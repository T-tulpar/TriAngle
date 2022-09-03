import math

"""
def sort_values(*args):
    list = []
    tuple = ()
    for i in args:
        list.append(i)
    list.sort(reverse=True)
    for i in list:
        tuple = tuple + (i,)

    return tuple

x=5
y=7
z=2

print(x,y,z)
print()

x,y,z=sort_values(x,y,z)

print(x,y,z)

x=5
y=3
z=2

def vls(*args):
    list = []
    tuple =()
    for i in args:
        i+=5
        list.append(i)
    for i in list:
        tuple = tuple + (i,)


    return tuple

print(x,y,z)
print()
x,y,z=vls(x,y,z)

print(x,y,z)
"""

x = 60
y = 70
z = 50

def cos1(a,c,b):
    return math.degrees(math.asin(((a*a)+(c*c)-(b*b))/(2*c*a))),math.degrees(math.asin(((a*a)+(b*b)-(c*c))/(2*b*a)))

cos1 = lambda a,b,c: (math.degrees(math.asin(((a*a)+(b*b)-(c*c))/(2*b*a))),math.degrees(math.asin(((a*a)+(c*c)-(b*b))/(2*c*a))))

def cos2(a, b, c, s=15):
    return round(math.sqrt(b * b + c * c - 2 * b * c * math.cos(math.radians(a))), s)  # Diğer kenarı buluyor
    # a= x açısı b= y kenarı c= z kenarı



def sin1(a,b,c):
    return a*math.sin(math.radians(c))/math.sin(math.radians(b))

def sin2(a, b, c):
    return math.degrees(math.asin(a * math.sin(math.radians(b)) / c))


print(cos1(5, 4, 3))

print(cos3(5, 4, 3))


#print('3' if 1-1==2 else '1+1=2 değilse')


