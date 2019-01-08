def oneAway(a,b):
    if (abs(len(a)-len(b))>1):
        return False
    if (abs(len(a)-len(b))<=1): #check differences of strings with legth difference of one or none
        if len(a)>len(b):
            c = list(set(list(a)) - set(list(b)))
        else:
            c = list(set(list(b)) - set(list(a)))
        if len(c)==1:
            return True


def a(a,b):
    c = list(set(list(a)) - set(list(b)))
    print(c)
