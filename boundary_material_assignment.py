#assign boundary materials instead of matrix to make sure cracks don't grow on edges
#need to manually add physical group to .msh file
#only works with tet meshes


#==

#1. READ THROUGH AND GRAB EDGE NODES
#2. FOR EACH NODE IN ELEMENT
#       A.  IS IT IN LIST OF EDGE NODES
#       B.  IF YES, CHANGE PHYSICAL GROUP!


#======================================
new_phys_id = '9'
inputmesh = open('mesh-manip\\no_bound.msh', 'r')

#======================================
#READ AND DETECT EDGE NODES, PUT IN A LIST
#======================================

node_list = 0
el_list = 0
physnames = 0
x_node_mat=[]
y_node_mat=[]
z_node_mat=[]
global list_list
list_list={}
elcount = 0


for line in inputmesh:
    

    if "$Nodes" in line[0:6]:
        node_list = 1
        #need to find the split

    elif node_list==1:
        #get_number of nodes
        number_of_nodes = int(line)
        node_list = 2

    elif '$EndNodeData' in line or "$EndNodes" in line:       
        print "Finding Node Maximums"

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


    #read the node data - 3 seperate columns to make max mins easier
    elif node_list == 2:
        line = line.replace("\n","")
        node_line = line.split(' ')
        x_node_mat.append(float(node_line[1]))
        y_node_mat.append(float(node_line[2]))
        z_node_mat.append(float(node_line[3]))


inputmesh.close()


#======================================
# see if elements have nodes in edge nodes list
# if so change physical group
#======================================

inputmesh = open('mesh-manip\\no_bound.msh', 'r')
outputmesh = open('mesh-manip\\yes_bound.msh', 'w')

for line in inputmesh:

    #read element data
    if "$Elements" in line[0:9]:
        outputmesh.write(line)
        el_list = 1

    elif el_list==1:

        outputmesh.write(line)
        el_list = 2

    elif el_list ==3:
        pass    #this is any extra junk at the end of the mesh file

    elif "$EndElements" in line:
        #start over for node data 
        el_list = 3 #means we done with elements
        outputmesh.write(line)
        print "Copied all Elements to String"
        
    elif el_list == 2:  #GET ALL ELEMENTS

        line = line.replace("\n","")
        el_line = line.split(' ')

        
        #el_line[0] = str(elcount) #renumber elements!
        #ellines += " ".join(el_line)+'\n' #need to create a full list to add to "new"
        #guiTest - justSaveAs - 

        if el_line[1] == '4': #type is tet, get 4 els
            type = 'tet'            
            start=5
            stop=8
            #check if min-maxes exist
            print "Checking Tet Elements: " + el_line[0]

            for el in el_line[start:stop+1]:
                for key in list_list:
                    if int(el) in list_list[key]:
                         el_line[3] = new_phys_id
                         el_line[4] = '20'

        #element list 
        #$Elements
        #number-of-elements
        #elm-number elm-type number-of-tags < tag > 
             #<tags> - when 3 = physical volume, physical volume, 0
        #node-number-list

        #elif el_line[1] == '5': #type is brick, get 8 els
        #    type = 'brick'
        #    start=6
        #    stop=13
        #    print "Checking Hex Elements: " + el_line[0]
        #    #check if min-maxes exist
        #    for key in list_list: #list_list is {xmax: allnodes, xmin: allnodes, }
        #        check_el_matrix(key, el_line[start:stop+1]) 


        el_line_new = " ".join(el_line) + "\n"
        outputmesh.write(el_line_new)

    else:
        outputmesh.write(line)

inputmesh.close()
outputmesh.close()