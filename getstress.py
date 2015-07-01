import sys
import os

#FOR HEXAGON LINCOLN TO PLOT THEIR RESULTS DATA (OR SOMETHING). 

#1.       Node numbers at location of data
#2.       Wind angle in radians (can read from FO data of input.ans?)
#3.       Radius (can read from $Nodes and "X" value)
#4.       Radial displacement (in y)
#5.       Axial strain (x)
#6.       Hoop or circumferential strain (z)
#7.       xz strain
#8.       Radial strain (y)
#9.       xy strain
#10.      yz strain

global node_matrix
node_matrix = []
node_list = 0
node_data = 0

local_r_global = raw_input("Local or Global (l or g): ")

#=========== vvv SHOULD COMMMENT vvv ==========
# THIS IS FOR PROBING THE LOCAL SCALE (ALL OUTPUTTED LOCAL RVES)
#===========================================



#=========== ^^^ SHOULD UNCOMMMENT  ^^^^ ==========


#dir = os.getcwd()
#In general to set the current working directory to the path given by the string, aPath:
os.chdir(wrkngd)

#for arg in sys.argv:
#    #f.write(str(arg))
#    pass
#name = arg.split(".")[0]

f = open("mesh-manip/ruslanres.msh",'r')
#f = open("files/ansys/New_Homog_00001.msh",'r')
#f = open(name+".msh",'r')
#w = open("files/ansys/res.csv", 'w')
w = open("mesh-manip/res.csv", 'w')
#print os.pathfiles = [f for f in os.listdir('.') if os.path.isfile(f)]


#clear out
node_matrix = []
node_list = 0
node_data = 0
reading="radius"

def write_to_node_matrix(id, key,value):
    #node_matrix[int(id)-1][key].append(value)
    #node_matrix[int(id)-1][key] = [value]
    try: 
        node_matrix[int(id)-1][key].append(value)
        
    except: #first time through (need a way to catch this)
        #node_matrix[int(id)-1].append(id)
        try:
            node_matrix[int(id)-1][key] = [value]
        except:
            a=1

for line in f:

    if "$Nodes" in line[0:6]:
        node_list = 1

    elif node_list==1:
        #get_number of nodes
        number_of_nodes = int(line)
        #instantiate node matrix
        for i in range(1, number_of_nodes+1):
            node_matrix.append({'id':i})
        node_list = 2

    elif '$EndNodeData' in line or "$EndNodes" in line:
        #start over for node data
        node_data = 0 
        node_list = 0

    #the type of "reading"
    elif node_data == 2:
        line = line.replace("\n","")
        reading = line.replace('"','')
        node_data = node_data + 1

    #read the node data
    elif node_data > 9 or node_list==2:
        #need to get the data and write it
        data = line.replace("\n","")
        data = data.split("\t")
        
        # Should we just probe one Node ID
        if probe_one:
            if data[0] == which_probe:
                write_to_node_matrix(data[0], reading, data[1])
            else:
                pass
        else:

            try:
                write_to_node_matrix(data[0], reading, data[1])

            except:
                a=1

        #if reading=="Displacements_sc0" or reading =="radius":
        #    write_to_node_matrix(data[0], reading, data[1])

        #else:  #"Stress_11_sc0", "Stress_22_sc0", "Stress_22_sc0", "Stress_12_sc0", "Stress_33_sc0"
        #"Strain_11_sc0", "Strain_22_sc0", "Strain_12_sc0", "Strain_33_sc0"

    elif "$NodeData" in line or node_data > 0:
        node_data = node_data + 1


#========= WRITE DATA ===================

if probe_one:
    len(node_matrix)
    iders = which_probe  #only thing i changed
    for stp in range(start,end):
        w.write("=====Step "+str(stp)+"======\n") #write a space between steps
        #for column in str(iders):  #gives you the column
        #    for layernum, ider in enumerate(column): #only works if iders [[1,2],[3,5]]

        #wipe out everything
        d=""
        c=""
        g=""
        a=""
        k=""
        #w.write("\n") #write a space between steps

        for id,key in enumerate(sorted(node_matrix[int(iders)-1])):   #get keys #sorted alphabetically

            d = d + str(key) + ","  #populate header
        
            try:
                a = node_matrix[int(iders)-1][key]   #for node, and given key

                #here's where i can define the tstep
                #=========
                #b=max(a)
                b = a[stp-1]
                #=========

                try:
                    #this gives hex comparison, i'm removing...
                    f = hex[id]
                    f = abs(f-float(b))/f
                    f = abs(f*100)
                    f = str(f)+"%"
                except:
                    f='n/a'
            except:
                #this flies if a is not a tuple
                try:
                    b = a[0]
                except:
                    b = a

            c = c + str(b) + "," 
            g = g + str(f) + "," 
            k = k + key + ","
    

        #hex_cases = "0.011808,0.017354,,,0.1402,,,-0.010238,,0.008643,"		

        w.write(c + "\n") #write the values  #write twice, for their output
        #w.write(k + "\n") 








else:

#========= WRITING IF WE ARE PRINTING ALL NODES OF GLOBAL IN LAYERS (NEED TO THINK MORE ABOUT IT) ================
    #c=[]
    #d=[]
    len(node_matrix)
    hex = [0.011808,0.017354,0,0,0.1402,0,0,-0.010238,0,0.008643]
    #for all keys

    iders =[[1,2,19,28,37,46],[3,4,20,29,38,47],[5,6,21,30,39,48],[7,8,22,31,40,49],[9,10,23,32,41,50],[11,12,27,36,45,54]]

    #steps=8  #number of steps, could get this programatically. 

    for stp in range(start,end):
    #range(1,11)
    #gives you
    #[1,2,3,4,5,6,7,8,9,10]

        w.write("=====Step "+str(stp+1)+"======\n") #write a space between steps

        for column in iders:  #gives you the column

            for layernum, ider in enumerate(column):

                #wipe out everything
                d=""
                c=""
                g=""
                a=""
                #w.write("\n") #write a space between steps

                for id,key in enumerate(node_matrix[0].keys()):   #get keys

                    d = d + str(key) + ","  #populate header
        
                    try:
                        a = node_matrix[ider-1][key]   #for node, and given key

                        #here's where i can define the step
                        #=========
                        #b=max(a)
                        b = a[stp]
                        #=========

                        try:
                            f = hex[id]
                            f = abs(f-float(b))/f
                            f = abs(f*100)
                            f = str(f)+"%"
                        except:
                            f='n/a'
                    except:
                        b = a

                    c = c + str(b) + "," 
                    g = g + str(f) + "," 
    

                #hex_cases = "0.011808,0.017354,,,0.1402,,,-0.010238,,0.008643,"		

                w.write(c + "\n") #write the values  #write twice, for their output
            
                if layernum == 1 or layernum == 2 or layernum == 3 or layernum == 4:  #could make this function of size of column matrix
                    w.write(c + "\n") #write the values
                    #w.write(hex_cases + "\n")
                    #w.write(g+"\n")
                    #w.write("\n\n")


w.write(d + "\n")  #write the headers
w.close()



#write it

#then going through you call

