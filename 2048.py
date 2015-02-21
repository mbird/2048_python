"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    for i in range(len(line)):
        result.append(0)

    merged = list(result) # list for keeping track which tiles have been merged
        
    j = 0 # index for result list
    for i in range(len(line)):
        if line[i] != 0:
            result[j] = line[i]
            if j > 0 and result[j] == result[j-1] and merged[j-1] != True:
                    result[j-1] += result[j]
                    result.pop(j)
                    result.append(0)
                    merged[j-1] = True
                    j -= 1
            j += 1
       
  
  
    
    return result

print merge([2, 2, 2, 2])
print merge([2, 0, 2, 4])
