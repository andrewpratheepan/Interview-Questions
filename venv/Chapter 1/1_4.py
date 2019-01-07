def PalindromePermutation(a):
    a = ''.join(sorted(a)).strip() #gets rid of spaces and puts it in alphabetical order
    print(a)
    limit = 1 #palindrom can have a maximum of one unique character
    i=0 #starts at index 0

    while (limit>=0):
        if i == len(a) - 1:
            if a[i] != a[i-1]:
                limit-=1
                break
        if limit == -1 or i >= len(a)-1:#checks if it reaches end of the string or can not return true
            break
        if a[i] == a[i+1]:
            i+=2
        elif a[i] != a[i+1]:
            limit -= 1
            i+=1
    return limit >= 0
