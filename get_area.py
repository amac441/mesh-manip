#Plug in three coordinates to triArea(a,b,c), and it will return the area of the triangle. 
#some common variable letters transfer into these meanings: m: slope y,c: y intercept a: x's coefficient b: y's coefficient

def dis(a,b):
    return (  (b[0]-a[0])**2 + (b[1]-a[1])**2   )**.5
def lineDis(m,y,point):
    """slope in decimal, y intercept, (x,y)"""
    a = m
    b = -1
    c = y
    m = point[0]
    n = point[1]
    return abs(a*m+b*n+c)/((a)**2+(b)**2)**.5
def findMY(a,b):
    """return slope(m), y intercept(y)"""
    x1,y1,x2,y2 = a[0],a[1],b[0],b[1]
    x1 = float(x1)
    y1 = float(y1)
    slope = (x2-x1)/(y2-y1)
    x,y=a[0],a[1]
    while x != 0:
        if x < 0:
            x+=1
            y += slope
        if x > 0:
            x-=1
            y-=slope
    yint = y
    return slope, yint
def triArea(a,b,c):
    h=dis(a,b)
    m,y = findMY(a,b)
    b=lineDis(m,y,c)
    return .5*h*b

#28306 2 2 7 46 3669 3671 3672
mesh = open('mesh-manip\\global.msh','r')
f = open('mesh-manip\\areas.txt', 'r')
node_list=0
x_node_mat = []
y_node_mat = []
z_node_mat = []

import math
def area2(a, b, c):
    def distance(p1, p2):
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

    side_a = distance(a, b)
    side_b = distance(b, c)
    side_c = distance(c, a)
    s = 0.5 * ( side_a + side_b + side_c)
    return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))


for line in mesh:

    if "$Nodes" in line[0:6]:
        node_list = 1

    elif node_list==1:
        #get_number of nodes
        print "entering nodes"
        node_list = 2

    elif '$EndNodeData' in line or "$EndNodes" in line:
        node_list = 0
        print "Finding Node Areas"
        
    #read the node data - 3 seperate columns to make max mins easier
    elif node_list == 2:
        try:
            line = line.replace("\n","")
            node_line = line.split(' ')
            x_node_mat.append(float(node_line[1]))
            y_node_mat.append(float(node_line[2]))
            z_node_mat.append(float(node_line[3]))
            
        except:
            a=1

cor = []
area=0
for line in f:

    try:
        line = line.replace("\n","")
        node_line = line.split(' ')
        node = (int(node_line[5]), int(node_line[6]), int(node_line[7]))
        cor = []

        for n in node:
            coord = (x_node_mat[n-1],y_node_mat[n-1],z_node_mat[n-1])
            cor.append(coord)

        ar = area2(cor[0],cor[1],cor[2])
        area += ar
        print "area = " + str(area)
    except:
        a=1

print "Full======= " + str(area)