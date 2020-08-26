'''
The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.

Sample 1.
Input:
2
Output:
2
2 = 1 + 1.
Sample 2.
Input:
28
Output:
6

'''
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
    
    
