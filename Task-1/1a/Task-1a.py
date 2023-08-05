x=open("input1a.txt","r")
y=open("output1a.txt","w")

l1=x.readline().split()
l1=[int(i) for i in l1]
v,e=l1

mat=[[0]*(v+1) for i in range(v+1)]

for run in range(e):
   lst=x.readline().split()
   lst=[int(i) for i in lst]
   n1,n2,cost=lst
   mat[n1][n2]=cost

for j in range(len(mat)):
    for i in range(len(mat[j])-1):        
        y.write(f"{mat[j][i]} ")
    if j==len(mat)-1:
        y.write(f"{mat[j][len(mat)-1]}")
    else:
        y.write(f"{mat[j][len(mat)-1]}\n")
    
y.close()

#Task1a-Solution
#1- First we create adjacency matrix with the help of the number of vertices
#2- Then we add the cost in that adjacency matrix
#3- Then to forming the adjacnecy matrix along with the values in the output.