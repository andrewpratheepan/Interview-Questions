def stringCompression(a):
    temp = a[0]
    b = ''
    counter = 0
    for i in range(len(a)):
       if a[i] == temp:
           counter+=1
       else:
           b += temp
           b += str(counter)
           counter =1
           temp = a[i]
    b += temp
    b += str(counter)
    if len(b) < len(a): #short length check
        return b
    return a
