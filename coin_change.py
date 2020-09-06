'''
Coin change problem Solved Dynamically
Given list of coins and a sum find out minimum coins to get that sum
'''
def coin_dynam(sum,coins,results):
    min_coins = sum
    if sum in coins:  #target in coin list itself
        results[sum] = 1
        return 1
    
    elif results[sum] > 0:  #returns if results has some values
        return results[sum]
    
    else:             #finding out min uisng recursion
        for i in [c for c in coins if c <= sum]:

            num_coins = 1 + coin_dynam(sum-i,coins,results)
            
            if num_coins < min_coins:
                #print(num_coins,min_coins)
                min_coins = num_coins
                
                results[sum] = min_coins
    #print(results)          
    return min_coins


coins = [1,2,5]
sum = 1000
results = [0]*(sum+1)

print(coin_dynam(sum,coins,results))