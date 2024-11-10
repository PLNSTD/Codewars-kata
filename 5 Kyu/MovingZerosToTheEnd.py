'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]'''

def move_zeros(lst):
    skipped = 0
    out = []
    for num in lst:
        if num == 0:
            skipped += 1
            continue
        out.append(num)
    out.extend([0] * skipped)
    return out