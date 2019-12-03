n = int(input())
arr = sorted(list(map(int, input().split())))
print(arr)
if n > 1:
    print(arr[-2])
else:
    print(arr[0])
