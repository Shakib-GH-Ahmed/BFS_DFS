x=open("input1b.txt","r")
y=open("output1b.txt","w")

l1=x.readline().split()
l1=[int(i) for i in l1]
v,e=l1

mat=[[0]*(v+1) for i in range(v+1)]

for run in range(e):
   lst=x.readline().split()
   lst=[int(i) for i in lst]
   n1,n2,cost=lst
   if mat[n1][n2] != 0:
       mat[n1].insert(n2, [cost,mat[n1].pop(n2)])
   else: 
    mat[n1][n2]=cost
   
for i in range(len(mat)):
    new_lst=[]
    for j in range(len(mat[i])):
        if mat[i][j] != 0:
            tag=False
            break
        else:
            tag=True
    if tag == True:
        y.write(f"{i} : \n")  
    else:
        y.write(f"{i} :  ") 
    
    for idx in range(len(mat[i])):
        if mat[i][idx] != 0:
            if type(mat[i][idx]) == list:
                new_lst.append(f"({idx},{mat[i][idx][0]}) ")
                new_lst.append(f"({idx},{mat[i][idx][1]}) ")               
            else:    
                new_lst.append(f"({idx},{mat[i][idx]}) ") 
    if new_lst != []:
        for  run in range(len(new_lst)-1):
            y.write(f"{new_lst[run]}")
        if i == len(mat)-1:
            y.write(f"{new_lst[-1]}")
        else:
            y.write(f"{new_lst[-1]}\n")
            
y.close()

#Task1b-Solution
#1- First we create adjacency matrix with the help of the number of vertices
#2- The line where edge between node and cost come the I gave a condition 
    #if there any cost already there in that n2 list it will create a list for not overlaping any number
#3- Next for loop indicates 
    # if we get 0, we go forward through the list
    #else we break the list
#4- Create a new list named new_lst where we appending the values, if it's a list we go through the index of the list 