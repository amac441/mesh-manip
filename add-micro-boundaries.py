import shutil

import Queue
import threading
import urllib2
    #element list 
    #$Elements
    #number-of-elements 
    #elm-number elm-type number-of-tags < tag > 
    #node-number-list

    #if e_type == "cps3":  #surface
    #    return "2 2 2 " + str(tag)  #not sure bout last number  - 3rd num is physical group

    #elif e_type == "t3d2":  #truss element
    #    return "1 2 1 " + str(tag) #not sure bout last number

    #elif e_type == "c3d4":   #Tet
    #    return "4 2 "+ str(physical_groups) +" 2"  #these four were always the same"
  
    #elif e_type == "c3d8":  #TYPE=C3D8 (brick)
    #    #1	5	3	2	2	0	 #last 3 are physical volume, physical volume, 0
    #                #3	3	0	
    #    return "5	3	2	2	0" #Eventually I will need a way to pass in physical groups
             #start = 6
             #stop = 13


#===== functions ==========
global el_matrix
el_matrix = {}
def write_el_matrix(maxmin,nodes):
    try: 
        el_matrix[maxmin].append(nodes) #assumes that el_matrix[maxmin] exists
        
    except: #first time through (need a way to catch this)
        try:
            el_matrix[maxmin] = [nodes]  #should give {maxmin: (values), maxmin2: (values)} 
        except:
            a=1

def check_el_matrix (maxmin, el_line):
    
    temp = [] #grows the node list for that element
    temper = False
    for i in list_list[maxmin]: #this is x_max, x_min list, etc.       
        
        for j in el_line:  #gets all nodes for that element line

            if i == int(j):  #if one of the edge nodes is in that element list, append it to temp!
                temp.append(i)
                temper = True
                #list_list[maxmin].remove(i)

    if temper == True:
        if len(temp) > 2:
            write_el_matrix(maxmin, temp)  #maxmin comes from calling the function - it is the boundary name
            #{xmax: [(1,2,3), (1,2,3)], xmin: [(1,2,3),(1,2,3)]}

f = open('mesh-manip\\local1.msh', 'r')
first = open('mesh-manip\\first.msh', 'w')
last = open('mesh-manip\\last.msh', 'w')
ellines = ""

#add boundaries=======

phys1='$PhysicalNames\n8\n2 2 "mmExtBoundary_Y_plus"\n2 3 "mmExtBoundary_Z_minus"\n2 4 "mmExtBoundary_Y_minus"\n2 5 "mmExtBoundary_X_minus\n'
phys2 = '2 6 "mmExtBoundary_X_plus"\n2 7 "mmExtBoundary_Z_plus"\n3 1 "Inclusion"\n3 8 "Matrix"\n$EndPhysicalNames\n'
physical_names = phys1 + phys2

#========node parsing========

node_list = 0
el_list = 0
physnames = 0
x_node_mat=[]
y_node_mat=[]
z_node_mat=[]
global list_list
list_list={}


for line in f:
    line = line.replace("\t", " ")

    if "$EndMeshFormat" in line:
        first.write(line)
        first.write(physical_names)

    elif '$PhysicalNames' in line:
        physnames = 1
    
    elif '$EndPhysicalNames' in line:
        physnames = 0

    elif physnames == 1:
        a=1

    elif "$Nodes" in line[0:6]:
        node_list = 1
        first.write(line)  #write first liner
        #need to find the split

    elif node_list==1:
        #get_number of nodes
        first.write(line)
        number_of_nodes = int(line)
        #instantiate node matrix
        #for i in range(1, number_of_nodes+1):
        #node_matrix.append({'id':i})
        node_list = 2

    elif '$EndNodeData' in line or "$EndNodes" in line:       
        print "Finding Node Maximums"

        ## called by each thread
        #def get_url(q, url):
        #    q.put(urllib2.urlopen(url).read())

        #nodes = [x_node_mat,y_node_mat,z_node_mat]

        #q = Queue.Queue()

        #for u in theurls:
        #    t = threading.Thread(target=getmax, args = (q,u))
        #    t.daemon = True
        #    t.start()

        #s = q.get()
        #print s
       
        first.write(line)
        #start over for node data 
        node_list = 0 #means we read elements

        #find maximums
        print "Finding x plus"
        x = max(x_node_mat)  #need to get the index here - not sure what it is - need internet
        x_max_list = [i+1 for i, j in enumerate(x_node_mat) if j == x]
        list_list['mmExtBoundary_x_plus']=x_max_list

        print "Finding y plus"
        y = max(y_node_mat)
        y_max_list = [i+1 for i, j in enumerate(y_node_mat) if j == y]
        list_list['mmExtBoundary_y_plus']=y_max_list
        
        print "Finding z plus"
        z = max(z_node_mat)
        z_max_list = [i+1 for i, j in enumerate(z_node_mat) if j == z]
        list_list['mmExtBoundary_z_plus']=z_max_list

        print "Finding x minus"
        x = min(x_node_mat)
        x_min_list = [i+1 for i, j in enumerate(x_node_mat) if j == x]
        list_list['mmExtBoundary_x_minus']=x_min_list

        print "Finding y minus"
        y = min(y_node_mat)
        y_min_list = [i+1 for i, j in enumerate(y_node_mat) if j == y]
        list_list['mmExtBoundary_y_minus']=y_min_list

        print "Finding z minus"
        z = min(z_node_mat)
        z_min_list = [i+1 for i, j in enumerate(z_node_mat) if j == z]
        list_list['mmExtBoundary_z_minus']=z_min_list


        # find max and min for the 3, and find All the indexes with that max and min, index+1 is the node id
        # using those node ids, need to create sufraces, but they must be related to the elements. 
        # so maybe the key is to find the elements that they corespond to, and the nodes in that element

        #send that list in to element find function

    #read the node data - 3 seperate columns to make max mins easier
    elif node_list == 2:
        first.write(line)
        line = line.replace("\n","")
        node_line = line.split(' ')
        x_node_mat.append(float(node_line[1]))
        y_node_mat.append(float(node_line[2]))
        z_node_mat.append(float(node_line[3]))
       

    #read element data
    elif "$Elements" in line[0:9]:
        first.write(line)
        el_list = 1

    elif el_list==1:

        #this is where i need to copy and start new
        first.close()
        shutil.copyfile('mesh-manip\\first.msh', 'mesh-manip\\first1.msh')
        first=open('mesh-manip\\first.msh','w')
        new=open('mesh-manip\\new.msh','w')
        #get_number of nodes
        #this NEEDS TO BE ADDED TO AND PRINTED TO NEW
        number_of_els = int(line)
        el_list = 2

    elif "$EndElements" in line:
        #start over for node data 
        el_list = 3 #means we done with elements
        first.write(line)

        print "Copied all Elements to String"

    elif el_list == 3:
        pass
        
    elif el_list == 2:
        ellines += line #need to create a full list to add to "new"

        line = line.replace("\n","")
        el_line = line.split(' ')

        if el_line[1] == '4': #type is tet, get 4 els
            type = 'tet'            
            start=5
            stop=8
            #check if min-maxes exist
            print "Checking Elements: " + el_line[0]


            q = Queue.Queue()

            for key in list_list: #list_list is {xmax: allnodes, xmin: allnodes, }
                t = threading.Thread(target=check_el_matrix, args = (key, el_line[start:stop+1]))
                t.daemon = True
                t.start()
            s = q.get()

                #check_el_matrix(key, el_line[start:stop+1]) 

        elif el_line[1] == '5': #type is brick, get 8 els
            type = 'brick'
            start=6
            stop=13
            print "Checking Elements: " + el_line[0]
            #check if min-maxes exist
            for key in list_list: #list_list is {xmax: allnodes, xmin: allnodes, }
                check_el_matrix(key, el_line[start:stop+1]) 

            #q = Queue.Queue()

            #for key in list_list: #list_list is {xmax: allnodes, xmin: allnodes, }
            #    t = threading.Thread(target=check_el_matrix, args = (key, el_line[start:stop+1]))
            #    t.daemon = True
            #    t.start()
            #s = q.get()

    else:
        first.write(line)

first.close()
#need to figure out how to print things
#print every line I read and learn things
#=======
count = 0
length = 0
for key in el_matrix:
    length += len(el_matrix[key])


incrementID = 40
typeID = 1

print "Writing and Merging Files"

new.write(str(number_of_els+length) + "\n")
new.write(ellines)

for key in el_matrix:
    incrementID +=1
    typeID += 1  
    for node_list in el_matrix[key]:  #gives (1,2,3) 
        count +=1
        if type == 'tet':
            new.write(str(number_of_els+count) + " 2 2 " + str(typeID) + " " + str(incrementID) + " " + str(node_list[0]) + " " + str(node_list[1]) + " " + str(node_list[2]) + "\n")
        elif type == 'brick':
        #1 3 2 4 15 6 5 3 2
            new.write(str(number_of_els+count) + " 3 2 " + str(typeID) + " " + str(incrementID) + " " + str(node_list[0]) + " " + str(node_list[1]) + " " + str(node_list[2]) + " " + str(node_list[3]) + "\n")

new.close()
     
#combine first1,new,first
#interpret material and fill out gmm
filenames = ['mesh-manip\\first1.msh','mesh-manip\\new.msh','mesh-manip\\first.msh']
with open('mesh-manip\\newboundary.msh', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

a=1

#2 2 2 2 41 54 23 65
#3 2 2 2 41 64 54 63

#======== writing the surface data ========
#for every element:
#    #are any of the maxes in that element

#    #create or append here:
#    el_edge_matrix = {'key elid'(1), 'value nodes'(12,3,4)}


#$Elements
##surface
#496
#1 2 2 2 41 64 26 54
#2 2 2 2 41 54 23 65
##volume
#282 4 2 8 3 64 79 86 3
#283 4 2 8 3 88 61 43 89
#284 4 2 8 3 88 61 92 43
#285 4 2 8 3 64 79 33 53

#Main concern for creating surfaces is knowing what the normal direction is


#go through mesh file
#for each node, decide if its a boundary 
   #  greatest and least for each of the 3 components
   #  if x1 is gt x_plus_master
   #  if x1 is lt x_minus_master
   #y_plus_master
   #z_plus_master
   #y_minus_master
   #z_minus_master

# have 3 arrays for x,y,z
# find max and min for the 3, and find All the indexes with that max and min, index+1 is the node id
# using those node ids, need to create sufraces, but they must be related to the elements. 
# so maybe the key is to find the elements that they corespond to, and the nodes in that element
# nodes need to share max component

#element 390
#surfaces 9 and 19
#nodes 51,66,24,70

