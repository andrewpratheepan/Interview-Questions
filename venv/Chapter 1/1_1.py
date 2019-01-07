def unique(str):
    for i in range(0,len(str)):
        for j in range(i+1,len(str)): #only values that have not been compared with i
            if str[i] == str[j]:
                return False
    return True
