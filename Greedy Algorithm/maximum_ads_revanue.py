'''
You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛
slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue
Task. 
    Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), 
    we need to partition them into 𝑛 pairs (𝑎𝑖, 𝑏𝑗 )such that the sum of their products is maximized.
Input Format.
    The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎1, 𝑎2, . . . , 𝑎𝑛, the third one contains a sequence of integers 𝑏1, 𝑏2, . . . , 𝑏𝑛.

Sample 1.
Input:
1
23
39
Output:
897
'''
def adsrevenue(n,a,b):
    a.sort()
    b.sort()
    c = [i*j for i,j in zip(a,b)]
    return sum(c)
    


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(adsrevenue(n,a,b))
