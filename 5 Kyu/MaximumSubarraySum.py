def max_sequence(arr):
    if not arr:  # If the list is empty
        return 0
    
    max_sum = 0
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum