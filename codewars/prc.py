def make_incrementor(n):
     return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

print(make_incrementor(42)(50))  #make...回傳一個lambda x: x+n 然後再給定(50做為x)