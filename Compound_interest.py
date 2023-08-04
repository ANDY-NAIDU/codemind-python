p, r, t = map(int, input().split())
result = p * (1 + (r / 100)) ** t
print(f"{result:.2f}")