def two_sum(arr, target):
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return 'No match'

a = [1,2,3,4]

print(two_sum(a,7))
print(two_sum(a,8))