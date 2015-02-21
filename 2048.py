"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    for ind in range(len(line)):
        result.append(0)

    merged = list(result) # list for keeping track which tiles have been merged
        
    jind = 0 # index for result list
    for ind in range(len(line)):
        if line[ind] != 0:
            result[jind] = line[ind]
            if jind > 0 and result[jind] == result[jind-1] and merged[jind-1] != True:
                    result[jind-1] += result[jind] # merge tiles
                    result.pop(jind) # remove second of the merged numbers
                    result.append(0) # fill up list to former length
                    merged[jind-1] = True
                    jind -= 1
            jind += 1
       
  
  
    
    return result

