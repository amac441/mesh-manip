
yp=[]
ym=[]
xp=[]
xm=[]
zp=[]
zm=[]
node_list=0
el_list=0
x_node_mat=[]
y_node_mat=[]
z_node_mat=[]
read = open('mesh-manip/full_mesh.msh','r')

for line in read:
    line = line.replace("\t", " ")

    if "$Nodes" in line[0:6]:
        node_list = 1
        #need to find the split

    elif node_list==1:
        #get_number of nodes
        print int(line)
        #instantiate node matrix
        #for i in range(1, number_of_nodes+1):
        #node_matrix.append({'id':i})
        node_list = 2

    elif '$EndNodeData' in line or "$EndNodes" in line:       
        #print s      
        #start over for node data 
        node_list = 0 #means we read elements


    #read the node data - 3 seperate columns to make max mins easier
    elif node_list == 2:
        line = line.replace("\n","")
        node_line = line.split(' ')
        x_node_mat.append(float(node_line[1]))
        y_node_mat.append(float(node_line[2]))
        z_node_mat.append(float(node_line[3]))

    #read element data
    elif "$Elements" in line[0:9]:
        el_list = 1

    elif el_list==1:

        #this NEEDS TO BE ADDED TO AND PRINTED TO NEW
        number_of_els = int(line)
        el_list = 2

    elif "$EndElements" in line:
        #start over for node data 
        el_list = 3 #means we done with elements

        print "Copied all Elements to String"

    elif el_list == 3:
        pass
        
    elif el_list == 2:
        #ellines += line #need to create a full list to add to "new"
        #2 2 "mmExtBoundary_Y_plus"
        #2 3 "mmExtBoundary_Z_minus"
        #2 4 "mmExtBoundary_Y_minus"
        #2 5 "mmExtBoundary_X_minus
        #2 6 "mmExtBoundary_X_plus"
        #2 7 "mmExtBoundary_Z_plus"

        line = line.replace("\n","")
        el_line = line.split(' ')

        if el_line[1] == '2': #type is surface
            
            if el_line[3] == '2':
                #elements{'xp':{(1,2,3),(1,2,3)
                yp.append(el_line[5])
                yp.append(el_line[6])
                yp.append(el_line[7])

            elif el_line[3] == '3':
                zm.append(el_line[5])
                zm.append(el_line[6])
                zm.append(el_line[7])

            elif el_line[3] == '4':
                ym.append(el_line[5])
                ym.append(el_line[6])
                ym.append(el_line[7])

            elif el_line[3] == '5':
                xm.append(el_line[5])
                xm.append(el_line[6])
                xm.append(el_line[7])

            elif el_line[3] == '6':
                xp.append(el_line[5])
                xp.append(el_line[6])
                xp.append(el_line[7])

            elif el_line[3] == '7':
                zp.append(el_line[5])
                zp.append(el_line[6])
                zp.append(el_line[5])

#surface element nodes - split by section, sort them and remove duplicates
yp=sorted(set(yp))
ym=sorted(set(ym))
xp=sorted(set(xp))
xm=sorted(set(xm))
zp=sorted(set(zp))
zm=sorted(set(zm))

#x test

f=open('mesh-manip/boundary2.txt','w')
count = 0 

for i in xp: #for a given node
    dir = '1' #x direction
    node = int(i)
    yn = y_node_mat[node-1]
    zn = z_node_mat[node-1]
    for j in xm:
        node2=int(j)
        yn2 = y_node_mat[node2-1]
        zn2 = z_node_mat[node2-1]
        if yn == yn2:
            if zn == zn2:
                if node!= 4586 and node !=2789 and node!=964 and node!=6354:  #NEED TO MAKE THESE INPUTS
                    #You have a winner!
                    count = count+1
                    string = "MFC_"+str(count)+" 2\n"+i+" "+dir+" 1.0\n"+j+" "+dir+" -1.0\n0.0\n\n"
                    f.write(string)

for i in yp: #for a given node
    dir = '2' #y direction
    node = int(i)
    yn = x_node_mat[node-1]
    zn = z_node_mat[node-1]
    for j in ym:
        node2=int(j)
        yn2 = x_node_mat[node2-1]
        zn2 = z_node_mat[node2-1]
        if yn == yn2:
            if zn == zn2:

                if node!= 1873 and node !=2789 and node!=5467 and node!=6354:  #NEED TO MAKE THESE INPUTS
                    #You have a winner!
                    count = count+1
                    string = "MFC_"+str(count)+" 2\n"+i+" "+dir+" 1.0\n"+j+" "+dir+" -1.0\n0.0\n\n"
                    f.write(string)

for i in zp: #for a given node
    dir = '3' #z direction
    node = int(i)
    yn = y_node_mat[node-1]
    zn = x_node_mat[node-1]
    for j in zm:
        node2=int(j)
        yn2 = y_node_mat[node2-1]
        zn2 = x_node_mat[node2-1]
        if yn == yn2:
            if zn == zn2:

                if node!= 4586 and node !=3669 and node!=5467 and node!=6354:  
                    #You have a winner!
                    count = count+1
                    string = "MFC_"+str(count)+" 2\n"+i+" "+dir+" 1.0\n"+j+" "+dir+" -1.0\n0.0\n\n"
                    f.write(string)

starter = "!MULTIFREEDOM_CONSTRAINTS_TBLOCK_ID!\n"+str(count)+'\n'

r=open('mesh-manip/boundary.txt','w')
r.write(starter)
f.close()
f=open('mesh-manip/boundary2.txt','r')
for line in f:
    r.write(line)

r.close()
f.close()

