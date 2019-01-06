def isStringPermutation(a,b):
    if (len(a) - len(b) != 0):
        return False #permutations must have same length
    #sorts strings (of same length
    Va = ''.join(sorted(a))
    Vb = ''.join(sorted(b))
    if Va==Vb:
        return True
    return False
