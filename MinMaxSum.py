def find_min_sum(arr, how_many_nums):
    min_sum = 0
    min_set = set()
    data_set = set(arr)
    for _ in range(how_many_nums):
        try:
            min_set.add(min(data_set.difference(min_set)))   
        except:
            break
    if len(min_set) < how_many_nums:
        min_sum = sum(min_set) + (sum(min_set)*(how_many_nums-len(min_set)))
    else:
        min_sum = sum(min_set)
    return min_sum

def find_max_sum(arr, how_many_nums):
    max_sum = 0
    max_set = set()
    data_set = set(arr)
    for _ in range(how_many_nums):
        try:
            max_set.add(max(data_set.difference(max_set)))
        except:
            break
    if len(max_set) < how_many_nums:
        max_sum = sum(max_set) + (sum(max_set) *(how_many_nums-len(max_set)))
    else:
        max_sum = sum(max_set)
    return max_sum
    
def miniMaxSum(arr, n):
    print (find_min_sum(arr, n), find_max_sum(arr, n)) 
