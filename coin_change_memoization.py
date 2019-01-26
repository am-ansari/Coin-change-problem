# -*- coding: utf-8 -*-

def rec_coin_memoization(target,denomination,cache):
    
    min_coins = target
    
    if target in denomination:
        cache[target] = 1
        return 1
    elif cache[target] > 0:
        return cache[target]
    else:
        for i in [c for c in denomination if c<= target]:
            
            num_coins = 1 + rec_coin_memoization(target - i, denomination, cache)
            
            if num_coins < min_coins:
                min_coins = num_coins
                cache[target] = min_coins
                
    return min_coins

target = 86
denomination = [1,5,10,15,25]
cache = [0]*(target+1)

print(rec_coin_memoization(target,denomination,cache))    