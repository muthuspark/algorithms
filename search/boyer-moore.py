def bad_character_table(pattern):
    # Create a dictionary to store the character table
    char_table = {}
    for i in range(len(pattern)):
        # Calculate the shift distance based on the 
        # position of the character in the pattern
        shift_distance = len(pattern) - 1 - i
        # Store the shift distance in the character 
        # table
        char_table[pattern[i]] = shift_distance
    return char_table

def good_suffix_table(pattern):
    offset_table = {}
    last_prefix_position = len(pattern)

    # Find the last prefix position for each suffix length
    for i in range(len(pattern), 0, -1):
        if is_prefix(pattern, i):
            last_prefix_position = i
        offset_table[len(pattern) - i] = last_prefix_position - i + len(pattern)

    # Find the suffix length for each position
    for i in range(len(pattern) - 1):
        slen = suffix_length(pattern, i)
        offset_table[slen] = len(pattern) - 1 - i + slen

    return offset_table

def is_prefix(pattern, p):
    """
    This method checks if the given pattern is a prefix of the
    pattern starting at position p. It compares the characters
    of the pattern from position p to the end of the pattern
    with the characters of the pattern from the beginning to
    position p. If all characters match, it returns True;
    otherwise, it returns False.
    """
    for i in range(p, len(pattern)):
        if pattern[i] != pattern[i - p]:
            return False
    return True

def suffix_length(pattern, p):
    """
    This method calculates the length of the suffix of the 
    pattern starting at position p. It compares the characters 
    of the pattern from the given position p to the end of the 
    pattern with the characters of the pattern from the end 
    to the given position p. It returns the length of the suffix
    that matches.
    """
    length = 0
    i = p
    j = len(pattern) - 1
    while i >= 0 and pattern[i] == pattern[j]:
        length += 1
        i -= 1
        j -= 1
    return length

def index_of(text, pattern):
    if len(pattern) == 0:
        return 0

    char_table = bad_character_table(pattern)
    offset_table = good_suffix_table(pattern)

    i = len(pattern) - 1
    itr = 1
    while i < len(text):
        j = len(pattern) - 1
        itr+=1
        while j >= 0 and pattern[j] == text[i]:
            i -= 1
            j -= 1

        if j < 0:
            return i + 1
        
        # This line updates the value of `i` by calculating the maximum 
        # shift distance based on the bad character rule and the 
        # good suffix rule.
        i += max(offset_table.get(len(pattern) - 1 - j, 0), 
                    char_table.get(text[i], -1))

    return -1

text = "TTATAGACTTTGTATTTCTCCTATTCTT"
pattern = "TCCTATTCTT"
result = index_of(text, pattern)

if result == -1:
    print("Pattern not found")
else:
    print("Pattern found at index:", result)

# Output:
# Pattern found at index: 18