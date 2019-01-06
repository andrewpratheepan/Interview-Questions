def URLify(a):
    for i in range(0,len(a)):
        if a.find(" ") == -1:
            break
        a = a[0:a.find(" ")] +"%20"+ a[a.find(" ")+1:]
    print(a)
