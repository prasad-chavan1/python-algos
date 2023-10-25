'''
Problem :
You are given a table with n rows and m columns. Each cell is colored with white or black. Considering the shapes created by black cells, 
what is the maximum border of these shapes? Border of a shape means the maximum number of consecutive black cells in any row or column 
without any white cell in between. A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.

Input format :
The first line contains t denoting the number of test cases.
The first line of each test case contains integers n, m denoting the number of rows and columns of the matrix. 
Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next n lines contains m integers.
'''
testCases = int(input())
l = []
for i in range(0, testCases):
    l = []
    l_count = []
    count = 0
    rolCol = input().split()
    for i in range(0, int(rolCol[0])):
        shapeStr = input()
        l.append(shapeStr)
    for item in l:
        count = 0
        for i in range(0, len(item)):
            if(item[i] == '#'):
                count += 1
        l_count.append(count)
    print(max(l_count))
