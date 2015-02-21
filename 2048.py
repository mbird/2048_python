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

    j = 0 # index for result list
    merged = False
    for i in range(len(line)):
        if line[i] != 0:
            result[j] = line[i]
            if j > 0 and result[j] == result[j-1] and merged == False:
                    result[j-1] += result[j]
                    result.pop(j)
                    result.append(0)
                    merged = True
                    j -= 1
            j += 1
       
  
            
    
    print line
    print result
    
    
    return []

merge([2, 0, 2, 4])
