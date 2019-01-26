# -*- coding: utf-8 -*-

def rec_coin(target,denomination):
    
    min_coins = target
    
    if target in denomination:
        return 1
    else:
        for i in [c for c in denomination if c<= target]:
            
            num_coins = 1 + rec_coin(target - i, denomination)
            
            if num_coins < min_coins:
                min_coins = num_coins
                
    return min_coins


print(rec_coin(86,[1,5,10,15,25]))    