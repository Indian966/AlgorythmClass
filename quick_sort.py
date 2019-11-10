S = [5, 8, 1, 3, 7, 2, 6, 9]

def quick_sorted(a):
    if len(a) > 1:
        pivot = a[len(a) - 1]
        left, mid, right = [], [], []
        for i in range(len(a) - 1):
            if a[i] < pivot:
                left.append(a[i])
            elif a[i] > pivot:
                right.append(a[i])
            else:
                mid.append(a[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return a

print(quick_sorted(S))
