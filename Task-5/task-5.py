x = open("input5.txt", "r")
y = open("output5.txt", "w")

from queue import Queue
l = x.readline().split()
l=[int(i) for i in l]
v, e, des =l
d = {}
for i in range(e):
    n1, n2 = x.readline().split()
    n1 = int(n1)
    n2 = int(n2)
    if n1 not in d.keys():
        d[n1] = [n2]
    else:
        d[n1].append(n2)
    if n2 not in d.keys():
        d[n2] = [n1]
    else:
        d[n2].append(n1)

color_lst = {}
visited = {}
p = {}
for i in range(v):
    color_lst[i+1] = "white"
    visited[i+1] = 0
    p[i+1] = None

def BFS(graph, n1, color_lst):
    Q = Queue() 
    color_lst[n1] = "gray"
    Q.put(n1)                
    while Q.empty() !=True:
        temp = Q.get()         
        
        if temp not in graph.keys():      
            continue
        else:
            for v in graph[temp]:        
                if color_lst[v] == "white":
                    color_lst[v] = "gray"
                    visited[v] = visited[temp]+1
                    p[v] = temp
                    Q.put(v)   
        color_lst[temp] = "black"
BFS(d, 1, color_lst)

print("Time:", visited[des], file = y)

final = []
n1 = des
while n1!= 1:
    final.append(n1)
    n1 = p[n1]
final.append(1)

print("Shortest Path:", end = " ", file = y)
i = len(final)-1
while i>-1:
    print(final[i], end = " ", file = y)
    i-=1
    
#we start the enque method after initializing the lst item to gray
#In the while loop (34 line), if it's not true we started dequeue
#Checking if temp is in the keys or not for the single vertice
#if its in the dictionary keys if run a loop of each vertice in the list and enqueue that
#if the color is already white it makes it gray and increment the value of that visited dictionary
#Initialize a new list and run a loop when it's not equal to 1, outside the loop we append 1
#append the values to the new list 'final' and it makes the output to the y file