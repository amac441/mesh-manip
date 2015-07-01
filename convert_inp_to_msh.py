#removes bar element elsets from a .INP file  (useful when we need to edit an RVE in hypermesh)

global physical_groups
#physical_groups = raw_input("Number of physical groups: ")
physical_groups = 1
#need to figure out a way to print this
#$MeshFormat
#2.2 0 8
#$EndMeshFormat
#$PhysicalNames
#3
#1 1 "a"
#2 2 "b"
#3 3 "c"
#4 4 "d"
#5 5 "e"
#$EndPhysicalNames
#================


import xml.etree.ElementTree as ET
import numpy as NP
from scipy import linalg as LA


f = open('files/inp/simple_out.msh','w') #the output file
r = open('files/inp/msh.inp', 'r') #the input file
#file = open('files/mold/outputa.xml','r')
e = ET.parse('files/inp/fo.xml')
header = "$MeshFormat\n2.1 0 8\n$EndMeshFormat\n\n"
f.write(header)

count = 0
tager=0
node_list = []
el_list =[]
node=1
El=False
head=True

#write header

#while not $node, replace


def convert(e_type, tag):

    #element list 
    #$Elements
    #number-of-elements 
    #elm-number elm-type number-of-tags < tag > 
    #node-number-list

    if e_type == "cps3":  #surface
        return "2 2 2 " + str(tag)  #not sure bout last number  - 3rd num is physical group

    elif e_type == "t3d2":  #truss element
        return "1 2 1 " + str(tag) #not sure bout last number

    elif e_type == "c3d4":   #Tet
        return "4 2 "+ str(physical_groups) +" 2"  #these four were always the same"
  
    elif e_type == "c3d8":  #TYPE=C3D8 (brick)
        #1	5	3	2	2	0	 #last 3 are physical volume, physical volume, 0
                    #3	3	0	
        return "5	3	2	2	0" #Eventually I will need a way to pass in physical groups

def split_list(a_list):
    #if len(a_list) > 1800:
    half = len(a_list)/2
    return "".join(a_list[:half]), "".join(a_list[half:]), True
    #else: 
    #    return "".join(a_list), [""], False 

for line in r:

    count = count+1

    if "*" in line:

            if "node" in line.lower() and node==1:  #meanse that this is first NODE
                node = 2
                node_start=count
                #a = line.replace("$","*")
                #node_list.append(a)

            elif "node" in line.lower():
                print "Two Nodes - " + str(line)
            
            elif "elset" in line.lower():  
                if node == 2:  #this is the end of the nodes, time to write
                    node_end = count   #this i the line number where nodes ends
                    #this number minus the node_start = number of nodes
                    node_count = node_end - node_start
                    node_count2 = len(node_list)
                    #node_list.insert(node_start+1, node_count)
                    #node_list = "".join(node_list)
                    f.write("$Nodes \n")
                    f.write(str(node_count2) + "\n")

                    #some fancy way to write the whole thing
                    #nodelist items have \n after each string
                    node_list = "".join(node_list)
                    f.write(node_list)

                    #for i in node_list:
                    #    f.write(i)
                    f.write("$EndNodes \n")
                    node = 3  #Done with nodes
                
                if "ype" in line.lower():   #should be the first of the Elsets
                    #Element Start Stuff
                    el = 2
                    if "elset" in line.lower():  #this tells the name of the element set             
                        tag = tager*3 + 1
                        tager = tager + 1                
                # Grab Type and Convert
                    e_type = line.lower()
                    e_type = e_type.split("type=",1)
                    e_type = e_type[1].split(",",1)
                    e_type = e_type[0]
                    e_type = convert(e_type, tag)
                    a=1
                else:
                    el = 3
            else:
                el = 3

    else:
        if node == 1 and head==True:  #do these things before we hit node list

            #print header and physical groups (ignore this for now)
            a=1

            #if physical_groups == 3:
            #    boundary = '2 2 "mmExtBoundary_Z_minus"\n'
            #else:
            #    boundary = ''
            
            #header = '$MeshFormat \n2.2 0 8 \n$EndMeshFormat \n$PhysicalNames \n'+str(physical_groups)+' \n1 1 "Inclusion" \n' + boundary + str(physical_groups) + ' ' + str(physical_groups) + ' "Matrix" \n$EndPhysicalNames \n'
            #f.write(header)
            #head = False

        elif node ==2: #do these things while in the node zone

            #convert to node format and collect
            n = line.replace(" ", "")
            n = n.replace(',',' ')
            node_list.append(n)           

        elif node ==3: #do these things while  in the element zone
            if el == 2:               
                #conver to el format and collect
                liner = line.replace(" ", "")
                liner = liner.replace(","," ")
                liner = liner.split(' ',1)
                el_line = liner[0] + " " + e_type + " " + liner[1]
                el_list.append(el_line)

        else:
            pass


els = len(el_list)
f.write("$Elements \n")
f.write(str(els) + "\n")
el_list = "".join(el_list)
f.write(el_list)

#this is if there are multiple physical groups, i'm repurposing node list, i dont need this
#el_list, node_list, D = split_list(el_list)
#f.write(el_list)
#f.write(node_list)

f.write("$EndElements")

#=====================
#CONVERT FO INTO FO.MSH
#=====================

#---------------------------------


tensors = [0,0,0,0,0,0]
count = 0
root = e.getroot()
data = root[1][4][1][1]
id = root[1][4][1]
evalsum = [0,0,0,0,0,0]
evecsum = [0,0,0,0,0,0]

#f = open('files/mold/small.txt','w')


#---------------------------------

def get_eigen(tensors):
    a = [[tensors[0],tensors[3],tensors[4]],[tensors[3],tensors[1],tensors[5]],[tensors[4],tensors[5],tensors[2]]]
    a = NP.array(a)
    b = a.reshape(3,3)
    #print b
    #print "-----------------------------------------"
    e_vals, e_vecs = LA.eig(b)
    e_vecs = e_vecs.real.tolist()
    e_vals = e_vals.real
    e_vals = e_vals.tolist()
    c = e_vals.index(max(e_vals))
    return e_vecs[c]

#----------------------------------
#GET EIGENS
#----------------------------------
eval = []
for j in data:
    count = count+1
    id = j.attrib
    id = id['ID']
    string = j.find('DeptValues').text

    a = [float(s) for s in string.split()]
    #print a
    evc = get_eigen(a)
    ee = []
    for e in evc:
        ee.append("\t" + str(e))

    evc = "".join(ee)
    eval.append(id + evc + "\n")


#---- Write header and all eigens ---
fos = len(eval)
eval = "".join(eval)

header = '\n$ElementData\n1\n"Fiber_Direction_sc0"\n1\n5\n4\n0\n3\n'+str(fos)+'\n0\n'
f.write(header)

f.write(eval)

f.write('$EndElementData\n')

f.close()
r.close()
a=1

            

    



