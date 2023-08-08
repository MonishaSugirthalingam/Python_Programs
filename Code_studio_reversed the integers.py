"""
input:
2 #number of test case
6 3 #first one number of elements and the 2nd one position
1 2 3 4 5 6
5 2
5 6 8 9 1
output:
1 2 3 4 6 5
5 6 8 1 9
"""
test_case=int(input())
for i in range(test_case):
    len_occ=input()
    elements=input()
    element=elements.split()
    for i in range(int(len_occ[0])):
        if i==int(len_occ[2]):
            occ=i=i+1
            element[occ],element[occ+1]= element[occ+1],element[occ]
    print(" ".join(element))
