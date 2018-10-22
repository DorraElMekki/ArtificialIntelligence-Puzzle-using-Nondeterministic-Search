'''
a. Formulate this puzzle as a state space search
*What are the states :
Considering our operations we have 16 possible states :
 (0,0) (10,0) (0,2) (2,0) (2,6) (8,0) (8,6) (10,4) (0,4) (4,0) (4,6) (10,6) (0,6) (6,0) (6,6) (10,2)

*The initial and goal states : 
	Initial state : (0,0) 
	Goal state : (8,y)  
we don’t care about the value of y. So it can be one of this possible values {0, 2, 4, 6}
*The operators :
We have 6 operators :
We suppose that :
	a is the level of water in jug A
	b is the level of water in jug B


    Operator	     Function
    ______________________________________
    Fill A	         a=10
    ______________________________________
    Fill B	         b=6
    ______________________________________
    Pour A into B 	 a = max (0, a +b-6 ) 
                     b = min (6, a+b )
    _____________________________________                 
    Pour B into A	 a = min (10, a+b ) 
                     b = max (0, a+b-10 )
    _____________________________________
    Dump A	         a=0
    ____________________________________
    Dump B	         b=0
    ____________________________________
*The branching factor :
In computing, tree data structures, and game theory, the branching factor is the number of children at each node, 
the outdegree. If this value is not uniform, an average branching factor can be calculated
We calculate the total number of possible states from each corrent state divided by the different possible next states
=> gives an average branching factor of 58/16=3.625

'''


#python 3.5.2
from random import randint
from numpy import *

######### our operators
def FillA(a,b,path):
    global RandomAccessQueue
    a=10
    path=path+'\nFillA(' + str(a)+','+str(b)+')'
    RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
    return 0

def FillB(a,b,path):
    global RandomAccessQueue
    b=6
    path=path+'\nFillB(' + str(a)+','+str(b)+')'
    RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
    return 0

def PourAB(a,b,path):
    global RandomAccessQueue
    x=max(0,a+b-6)
    b=min(6,a+b)
    a=x
    path=path+'\nPourAB(' + str(a)+','+str(b)+')'
    RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
    return 0

def PourBA(a,b,path):
     global RandomAccessQueue
     x=min(10,a+b)
     b=max(0,a+b-10)
     a=x
     path=path+'\nPourBA(' + str(a)+','+str(b)+')'
     RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
     return 0
        
def DumpA(a,b,path): 
    global RandomAccessQueue
    a=0
    path=path+'\nDumpA(' + str(a)+','+str(b)+')'
    RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
    return 0

def DumpB(a,b,path):
    global RandomAccessQueue
    b=0
    path=path+'\nDumpB(' + str(a)+','+str(b)+')'
    RandomAccessQueue= append(RandomAccessQueue,[[a,b,path]],0)
    return 0
##########
def TryAll(a,b,path):
    global SizeRandomAccessQueue   
    FillA(a,b,path)
    FillB(a,b,path)
    PourAB(a,b,path)
    PourBA(a,b,path)
    DumpA(a,b,path)
    DumpB(a,b,path)
    SizeRandomAccessQueue=SizeRandomAccessQueue+6
    return 0
#########
White=0 #no visited
Black=1 #visited

#initialize all states as no visited
rows =11
columns= 7
Visited = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
    for j in range(columns):
        Visited[i][j] = White


RandomAccessQueue= []
RandomAccessQueue.append([0, 0,'InitialState(0 0)']) #initial state 
SizeRandomAccessQueue=1

i=1
while SizeRandomAccessQueue>0:

 
 RandomIndex=randint(0,SizeRandomAccessQueue-1)
 JugALevel=int(RandomAccessQueue[RandomIndex][0])
 JugBLevel=int(RandomAccessQueue[RandomIndex][1])
 Path=RandomAccessQueue[RandomIndex][2] 
 

 if(Visited[int(JugALevel)][int(JugBLevel)]==Black):
  RandomAccessQueue=delete(RandomAccessQueue,[RandomIndex],0)
  SizeRandomAccessQueue=SizeRandomAccessQueue-1 
 else:
  Visited[JugALevel][JugBLevel]=Black
  TryAll(JugALevel,JugBLevel,Path)
  RandomAccessQueue=delete(RandomAccessQueue,[RandomIndex],0)
  SizeRandomAccessQueue=SizeRandomAccessQueue-1

 if (JugALevel==8):
  print(Path) 
  break



