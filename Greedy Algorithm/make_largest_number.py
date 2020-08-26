def make_largest_number(n,digits):
    digits.sort()
    digits.sort(key=lambda x: int(x[0]),reverse=True)
    return int("".join(digits))
n = int(input())
digits = input().split()
print(make_largest_number(n,digits))
