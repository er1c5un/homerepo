nums = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def merge_sort_my(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort_my(arr[:mid])
        right = merge_sort_my(arr[mid:])
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


print(f'nums {nums}')
res = merge_sort_my(nums)
print(f'nums {res}')
