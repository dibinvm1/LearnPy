'''
Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.
It returns the count of pairs and prints the pairs
'''

def pair_sum(arr,k):
    seen = set()
    output = set()
    for x in arr:
        if (len(arr) < 2):
            return
        for x in arr:
            target = k-x
            if not target in seen:
                seen.add(x)
            else:
                output.add(( min(x,target) ,max(x,target)) )
    print('\n'.join(map(str,list(output))))
    return len(output)

res = pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
print(res)