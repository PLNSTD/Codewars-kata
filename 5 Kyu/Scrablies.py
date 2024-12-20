def scramble(s1, s2):
    occ = {}
    for char in s2:
        occ[char] = occ.get(char, 0) + 1
    for char in s1:
        occ[char] = occ.get(char, 0) - 1
        
    for key in occ:
        if occ[key] > 0:
            return False
    
    return True