'''
Given two arrays (second array is formed by shuffling the elements of the first array and deleting a random element)
find which element is missing in the second array. 
'''
#Algo 1 - time : O(n) space : O(n)
#same logic as anagram py..using DeafaultDictionary 
import collections

def find_missing1(arr1, arr2): 
    d=collections.defaultdict(int) 
    for num in arr2:  #searching and adding to Dictionary from arr2(lesser one)
        d[num]+=1 
    
    for num in arr1: #searching and substracting in Dictionary from arr1
        if d[num]==0: 
            return num  # returning the missing number since it's not found in Dictionary
        else: d[num]-=1 

#Algo 2 - time : O(n) space : O(1)
#XOR all numbers in both lists + 0
def find_missing2(arr1, arr2): 
    res=0 
    for num in arr1+arr2:
       # print(res) 
        res^=num  #XORing
       # print(f'{res} XOR = {num}')
    return res
if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [3,7,2,1,4,6]
    print(find_missing1(arr1,arr2))
    print(find_missing2(arr1,arr2))