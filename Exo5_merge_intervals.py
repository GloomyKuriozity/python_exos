"""
PROGRAM NAME - merge_intervals
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 03/08/2023
NDP - None :)
"""



def merge_intervals(intervals):
    """
    Will take a list of intervals and will merge the overlapping intervals.
    
    Args:
        intervals (list): list of intervals to test.
    
    Returns:
        merged (list): list of intervals merged if necessary.
    """
    
    merged = []
    check = 0
    intervals = sorted(intervals)
    
    for i in range(1,len(intervals)):
        if check == 0:
            if intervals[i-1][1] >= intervals[i][0]:
                merged.append([intervals[i-1][0], intervals[i][1]])
                check = 1
            else:
                merged.append(intervals[i-1])
        else:
            check = 0
        
    if check == 0:
        merged.append(intervals[i])
            
    return merged
    
    
# Test the function
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
