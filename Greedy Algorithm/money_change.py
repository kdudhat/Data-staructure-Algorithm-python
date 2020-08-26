amount = int(input())
coin = 0
if amount>=10:
    rest_amount = amount%10
    amount -= rest_amount
    coin += amount//10
    amount = rest_amount
if amount>=5:
    amount-=5
    coin+=1
if amount<5:
    coin+=amount
        
print(coin)        
    
    
