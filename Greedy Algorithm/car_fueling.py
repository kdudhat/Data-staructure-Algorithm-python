'''
You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel
at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop1,stop2, . . . ,stop𝑛 from your home city. What is the minimum number of refills needed?

Input Format
          The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
          specifies an integer 𝑛. Finally, the last line contains integers stop1,stop2, . . . ,stop𝑛.
Output Format
          Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
          on a full tank, and there are gas stations at distances stop1,stop2, . . . ,stop𝑛 along the way, output the
          minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
          reach the destination, output −1.
          
 Sample 1.
Input:
950
400
4
200 375 550 750
Output:
2

The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices to make two refills: at points 375 and 750.
This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.
'''
def minrefills(x,n,L):
    numRefills = 0
    currentRefill = 0
    while currentRefill<=n:
        lastRefill=currentRefill
        while currentRefill<=n and x[currentRefill+1]-x[lastRefill]<=L:
            currentRefill+=1
        if currentRefill == lastRefill:
            return -1
        if currentRefill<=n:
            numRefills+=1
    return numRefills
d = int(input())
L = int(input())
n = int(input())
x =[0]+ list(map(int,input().split())) + [d]
print(minrefills(x,n,L))
