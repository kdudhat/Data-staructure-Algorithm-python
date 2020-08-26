'''
Input Format. 
            The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.

Output Format.
             Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
Sample 1.
Input:
2
21 2
Output:
221

Sample 2.
Input:
5
9 4 6 1 9
Output:
99641


'''
def make_largest_number(n,digits):
    digits.sort()
    digits.sort(key=lambda x: int(x[0]),reverse=True)
    return int("".join(digits))
n = int(input())
digits = input().split()
print(make_largest_number(n,digits))
