f = open("matrix_fiber.mesh", 'r')
n = open("matrix_fiber.msh", 'w')

#=====
starter = "$MeshFormat\n2.2 0 8\n$EndMeshFormat\n$PhysicalNames\n"
groups = 1

#5
#0 4 "ypluspoint"
#1 1 "internal"
#1 2 "ymin"
#1 3 "yplus"
#2 5 "layer"

ender = "$EndPhysicalNames\n$Nodes"

count = 0
elements = False
nodes==True

for line in f:

    if elements == True:
        hex_number = line.replace('\n','')
        hex_number = int(hex_number)
        nodes=False
        elements=False
        f.write("$Elements \n")
        f.write(str(hex_number) + "\n")

    elif count < 2:
        count += 1

    elif count == 4:
        nodes = line.replace('\n','')
        nodes = int(nodes)
        count += 1

    elif "hex" in line:
        #elements count
        elements = True

    elif count > 4 and nodes==True:
        #read nodes
        a=1

    else:
        #reading elements
        els = line.replace('\n','')
        els = els.split(' ',8)
        

n.write('$EndElements \n')
#======== JUST NEED HEX =====
    #element list 
    #$Elements
    #number-of-elements
    #elm-number elm-type number-of-tags < tag > 
         #<tags> - when 3 = physical volume, physical volume, 0
    #node-number-list

    elif e_type == "c3d8":  #TYPE=C3D8 (brick)
        #1	5	3	2	2	0	 #last 3 are physical volume, physical volume, 0
                    #3	3	0	
        return "5	3	2	2	0" #Eventually I will need a way to pass in physical groups
    56 2 2 2 25 55 71 64


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