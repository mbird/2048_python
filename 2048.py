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

    j = 0 # indes for result list
    for i in range(len(line)):
        if line[i] != 0:
            result[j] = line[i] 
            j += 1
       
            
            
    
    print line
    print result
    
    
    return []

merge([2,0,0,0,2,4])
