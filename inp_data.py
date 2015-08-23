#header = "*HEADING \nFinite Element Mesh\nFrom map\n*NODE, NSET=NAll \n"
#inp.write(header)

##nodes----
#1, -0.143509, -0.457903, -0.596397
#2, 0.634728, 0.0349801, -0.207278


#inp.write("*ELEMENT, TYPE=CPE4, ELSET=EAll"  + "\n")  

#acceptable elements
    #**                 LIST OF SOME ELEMENT TYPES
    #**                        CPE3         3 noded plane strain triangle
    #**                        CPE4         4 noded plane strain quadrilateral
    #**                        CPE6         6 noded plane strain triangle
    #**                        CPE8         8 noded plane strain quadrilateral
    #**                        CPS3         3 noded plane stress triangle
    #**                        CPS4         4 noded plane stress quadrilateral
    #**                        CPS6         6 noded plane stress triangle
    #**                        CPS8         8 noded plane stress quadrilateral
    #**                        C3D4         4 noded tetrahedron
    #**                        C3D6         6 noded triangular prism
    #**                        C3D8         8 noded brick
    #**                        C3D10        10 noded tetrahedron
    #**                        C3D15        15 noded triangular prism
    #**                        C3D20        20 noded brick
    #**                 For problems involving large plastic strains or nearly incompressible
    #**                 materials, add suffix R or H to element type (eg CPE4R, C3D4H)
    #**                 to use reduced integration (R) or hybrid element (H)
    #**
    #**
    #**     COHESIVE ELEMENTS
    #**
    #**         In summary, COH2D6, COH3D9 and COH3D12 cannot be converted into multimech.
    #**
    #**          COH2D4          4 noded 2D line interface element
    #**          COHAX4          4 noded 2D line interface element
    #**          COH3D6          6 noded 3D triangle interface element
    #**          COH3D8          8 noded 3D quadrilateral interface element


#elements ---
#
#1, 1, 3
#2, 3, 4
#3, 4, 5
#4, 5, 2
#*Element, type=CPS3, ELSET=Surface10
#37, 49, 72, 58
#38, 49, 59, 72
#39, 47, 73, 52
#*ELEMENT,TYPE=CPS4,ELSET=EAll
#         1, 3, 1, 2, 4
#         2, 5, 3, 4, 6
#*Element, type=C3D4, ELSET=Volume2
#277, 148, 142, 145, 28
#278, 197, 184, 13, 209
#279, 199, 194, 28, 39
#280, 134, 26, 175, 194

##element and nodesets
#inp.write("*ELSET, ELSET=Layer" + key + "\n\t")

#*ELSET,ELSET=Inclusion
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
#21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 