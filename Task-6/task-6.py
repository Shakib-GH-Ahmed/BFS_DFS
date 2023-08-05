x = open("input6.txt", "r")
y = open("output6.txt", "w")

l = x.readline().split()
l=[int(i) for i in l]
row,col=l

s1 = 0
s2 = 0
diamond = 0
new_lst = []
mat = []

for i in range(row):
    store = x.readline().strip("\n")
    mat.append(store)

clr = {}
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == "#":
            clr[i, j] = "black"
        else:
            clr[i, j] = "white"

def search(mat, s1, s2, diamond):

    clr[s1, s2] = "black"
    if mat[s1][s2] == "D":
        diamond += 1
        new_lst.append(diamond)

    while "white" in clr.values():
        if s2-1>-1 and (mat[s1][s2-1] == "." or mat[s1][s2-1] == "D") and clr[s1, s2-1] == "white":
            search(mat, s1, s2-1, diamond)
        elif s2+1<col and (mat[s1][s2+1] == "." or mat[s1][s2+1] == "D") and clr[s1, s2+1] == "white":
            search(mat, s1, s2+1, diamond)
        elif s1+1<row and (mat[s1+1][s2] == "." or mat[s1+1][s2] == "D") and clr[s1+1, s2] == "white":
            search(mat, s1+1, s2, diamond)
        elif s1-1>-1 and (mat[s1-1][s2] == "." or mat[s1-1][s2] == "D") and clr[s1-1, s2] == "white":
            search(mat, s1-1, s2, diamond)
        else:
            diamond = 0
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if clr[i, j] == "white":
                        search(mat, i, j, diamond)

search(mat, s1, s2, diamond)

high = 0
for i in range(len(new_lst)):
    if new_lst[i] > high:
        high = new_lst[i]
        
y.write(f"{high}")
y.close()

#2 variable takes the row and column value
#run a loop with row value and append next line inputs to the 'mat' list 
#run nested loop, 
    # if it matches '#', setting the dictionary key value to black
    #else, setting the dictionary key value to white
#In the function for finding 'D' we incrementing the diamond count and append to new list
#for each white in the dictionary values, we use condition and each of the conditions takes a recursive call