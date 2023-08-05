x = open("input4.txt", "r")
y = open("output4.txt", "w")

from queue import Queue

l1 = x.readline().split()
l1=[int(i) for i in l1]
v,e=l1
dictn = {}
dic_clr = {}
new_lst = []

for run in range(e):
    lst= x.readline().split()
    if len(lst) != 1:
        lst=[int(i) for i in lst]
        n1,n2=lst
        if n1 in dictn.keys():
            dictn[n1].append(n2)
        else:
            dictn[n1] = [n2]

for j in range(v):
    dic_clr[j+1] = "white"


def DFS(graph):
    for n1 in dic_clr.keys():
        if dic_clr[n1] == "white":
            Color_DFS(graph, n1)

def Color_DFS(graph, n1):
    dic_clr[n1] = "gray"
    if n1 in dictn.keys():
        for v in dictn[n1]:
            if dic_clr[v] == "white":
                cycle = "NO"
                new_lst.append(cycle)
                Color_DFS(graph, v)
            elif dic_clr[v] == "gray":
                cycle = "YES"
                new_lst.append(cycle)
                break
            else:
                cycle = "NO"
                new_lst.append(cycle)
    dic_clr[n1] = "black"

DFS(dictn)
if "YES" in new_lst:
    print("YES", file = y)
else:
    print("NO", file = y)
    
y.close()

#Initializing two dictionary and one list
#1st dictionary takes the key as n1 and value as n2
#2nd dictionary makes all color to white at first
#In the function(DFS) for the white color it calls the function(Color_DFS) recursively
#if the n1 matches with the 1st dictionary keys we run a loop in the dictionary index
#It allows three conditions inside the loop and finds the cycle
#if it not enters the condition of the keys it makes the color of that node to black