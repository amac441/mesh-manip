
#$PhysicalNames
#4
#2 3 "yplus"
#2 4 "ymin"
#3 1 "top"  - tet mesh
#3 2 "bottom"  - hex mesh

#==========
#0 10 "ypluscenter"  - point
#1 1 "internal"  - line
#2 5 "layer1" - 2d element

#$EndPhysicalNames

##===Points ======
#1 15 2 4 17 17   
#2 15 2 4 54 54   

##===Lines ======  just connects multiple points under same phys group
#7 1 2 2 2 1 2  
#8 1 2 2 2 2 19  
#9 1 2 2 2 19 28  
#10 1 2 2 2 28 37  

##====Surface Elements ===
#1 2 2 4 37 3 10 9
#2 2 2 4 37 10 3 2
^^^
triang surface
vvv
#3 2 2 3 45 1 12 11
#4 2 2 3 45 12 1 4

#5 3 2 4 15 6 5 3 2
^^^^
quad surface
vvv
#6 3 2 3 23 7 1 4 8



##==== 3d elements ====
##===== Tet =====
#7 4 2 1 2 12 1 4 13
##=====Hex============
#19 5 2 2 1 6 2 3 5 7 1 4 8

#===================
#1472 5 2 0 1 1979 1923 1937 1951 1980 1924 1938 1952
#1473 5 2 0 2 9 1989 1995 77 10 1990 1996 78
#         ^
#         this valueue is physical name



#=== 2d ===

$MeshFormat
2.2 0 8
$EndMeshFormat
$PhysicalNames
10
0 4 "ypluspoint"
0 10 "ypluscenter"
1 1 "internal"
1 2 "ymin"
1 3 "yplus"
2 5 "layer1"
2 6 "layer2"
2 7 "layer3"
2 8 "layer4"
2 9 "layer5"
$EndPhysicalNames
$Nodes
54
1 8.0 0.0 0 
2 8.02875 0.0 0
3 8.0 0.125 0
4 8.02875 0.125 0
5 8.0 0.25 0
6 8.02875 0.25 0
7 8.0 0.375 0
8 8.02875 0.375 0
9 8.0 0.5 0
10 8.02875 0.5 0
11 8.0 0.625 0
12 8.02875 0.625 0
13 8.0 0.75 0
14 8.02875 0.75 0
15 8.0 0.875 0
16 8.02875 0.875 0
17 8.0 1.0 0
18 8.02875 1.0 0
19 8.057504 0.0 0
20 8.057504 0.125 0
21 8.057504 0.25 0
22 8.057504 0.375 0
23 8.057504 0.5 0
24 8.057504 0.625 0
25 8.057504 0.75 0
26 8.057504 0.875 0
27 8.057504 1.0 0
28 8.086263 0.0 0
29 8.086263 0.125 0
30 8.086263 0.25 0
31 8.086263 0.375 0
32 8.086263 0.5 0
33 8.086263 0.625 0
34 8.086263 0.75 0
35 8.086263 0.875 0
36 8.086263 1.0 0
37 8.115027 0.0 0
38 8.115027 0.125 0
39 8.115027 0.25 0
40 8.115027 0.375 0
41 8.115027 0.5 0
42 8.115027 0.625 0
43 8.115027 0.75 0
44 8.115027 0.875 0
45 8.115027 1.0 0
46 8.143794 0.0 0
47 8.143794 0.125 0
48 8.143794 0.25 0
49 8.143794 0.375 0
50 8.143794 0.5 0
51 8.143794 0.625 0
52 8.143794 0.75 0
53 8.143794 0.875 0
54 8.143794 1.0 0
$EndNodes
$Elements
64
1 15 2 4 17 17   
2 15 2 4 54 54   
3 15 2 10 18 18   
4 15 2 10 27 27   
5 15 2 10 36 36   
6 15 2 10 45 45   


1 2 "ymin"
7 1 2 2 2 1 2  
8 1 2 2 2 2 19  
9 1 2 2 2 19 28  
10 1 2 2 2 28 37  
   ^   ^ ^
   type id notsure

11 1 2 2 2 37 46  
12 1 2 1 3 1 3 
20 1 2 3 4 17 18 
3633 1 2 3 3 2093 2195

1 1 "internal"
12 1 2 1 3 1 3  
13 1 2 1 3 3 5  
14 1 2 1 3 5 7  
15 1 2 1 3 7 9  
16 1 2 1 3 9 11  
17 1 2 1 3 11 13  
18 1 2 1 3 13 15  
19 1 2 1 3 15 17  

1 3 "yplus"
20 1 2 3 4 17 18  
21 1 2 3 4 18 27  
22 1 2 3 4 27 36  
23 1 2 3 4 36 45  
24 1 2 3 4 45 54  

25 3 2 5 6 3 1 2 4
26 3 2 5 6 5 3 4 6
27 3 2 5 6 7 5 6 8
28 3 2 5 6 9 7 8 10
29 3 2 5 6 11 9 10 12
30 3 2 5 6 13 11 12 14
31 3 2 5 6 15 13 14 16
32 3 2 5 6 17 15 16 18
2 6 "layer2"
33 3 2 6 6 4 2 19 20
34 3 2 6 6 6 4 20 21
35 3 2 6 6 8 6 21 22
36 3 2 6 6 10 8 22 23
37 3 2 6 6 12 10 23 24
38 3 2 6 6 14 12 24 25
39 3 2 6 6 16 14 25 26
40 3 2 6 6 18 16 26 27
2 7 "layer3"
41 3 2 7 6 20 19 28 29
42 3 2 7 6 21 20 29 30
43 3 2 7 6 22 21 30 31
44 3 2 7 6 23 22 31 32
45 3 2 7 6 24 23 32 33
46 3 2 7 6 25 24 33 34
47 3 2 7 6 26 25 34 35
48 3 2 7 6 27 26 35 36
49 3 2 8 6 29 28 37 38
50 3 2 8 6 30 29 38 39
51 3 2 8 6 31 30 39 40
52 3 2 8 6 32 31 40 41
53 3 2 8 6 33 32 41 42
54 3 2 8 6 34 33 42 43
55 3 2 8 6 35 34 43 44
56 3 2 8 6 36 35 44 45
57 3 2 9 6 38 37 46 47
58 3 2 9 6 39 38 47 48
59 3 2 9 6 40 39 48 49
60 3 2 9 6 41 40 49 50
61 3 2 9 6 42 41 50 51
62 3 2 9 6 43 42 51 52
63 3 2 9 6 44 43 52 53
64 3 2 9 6 45 44 53 54
$EndElements