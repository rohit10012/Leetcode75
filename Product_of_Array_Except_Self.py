# arr = [1,3,5,6,8]
arr = [1,2,3,0,4]
brr = []
result = 1
zero_count = 0

for n in arr:
    if n == 0:
        continue
    result = result * n

for m in arr:
    if m == 0:
        zero_count += 1
        brr.append(result)
        continue
    elif m != 0 and zero_count == 1:
        l = 0
        brr.append(l)
    else:
        l = int(result / m)
        brr.append(l)

print(brr)

