def high(x):
    # Code here
    max_word = ''
    max_points = 0
    for word in x.split():
        word_points = sum(ord(char)-96 for char in word.lower())
        if word_points > max_points:
            max_points = word_points
            max_word = word
    return max_word