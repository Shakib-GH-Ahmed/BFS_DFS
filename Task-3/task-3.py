x=open("input3.txt","r")
y=open("output3.txt","w")

from queue import Queue

l1=x.readline().split()
l1=[int(i) for i in l1]
v,e=l1

mat=[[0]*v for i in range(v)]
dic={}

for run in range(e):
   lst=x.readline().split()
   lst=[int(i) for i in lst]
   n1,n2=lst
   mat[n1-1][n2-1] = 1
   mat[n2-1][n1-1] = 1
 
for idx in range(v):
    dic[idx+1] = "White"
    
def DFS(G,n1,dic):
    dic[n1] = "Black"
    y.write(f"{n1} ")
    for j in range(len(G[n1-1])):
        if G[n1-1][j] != 0:
            if dic[j+1] == "White":
                DFS(G,j+1,dic)
                               
DFS(mat,1,dic)
y.close()

#Task-3 Solution
#1- creating adjacency matrix and adding the bidirectional road to the list using n1,n2
#2- initially all the vertices would be White
#3- In the method whenever we entering, we setting up the color of the vertices in the list to Black
    #in the loop we deonating each vertices of the adjacency list
    #if the color of the verice is White, we use recursion to get back to the DFS method