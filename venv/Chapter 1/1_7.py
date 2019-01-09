import pprint
def rotateMatrix(a):#a is nXn
    b = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i].append(a[i])
'''
def test():
    b = []
    for i in range(6):
        b.append([])
        for j in range(6):
            b[i].append(1)
    for i in range(len(b)):
        print(b)'''


    #TODO Q1_7