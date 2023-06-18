def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right

# Test cases
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
