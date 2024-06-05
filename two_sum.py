

a = [1,4,2,6,9]
sum = 8

for i in a:
    i = 1
    if a[i-1] + a[i] == sum:
        print(i-1,i)
        i += 1