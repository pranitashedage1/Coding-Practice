# if input is 17 then square root is 4. something...
# if input is 16 then square root is 4

def find_square_root(start, square):
    end = square
    while start <= end:
        mid = (start + end)//2
        if mid * mid == square:
            return mid
        elif mid * mid < square:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

a = find_square_root(1, 27)
print(a)
