def solution(x1, y1, x2, y2, xl, yl, R):
    def inside(x, y):
        return (x - xl) ** 2 + (y - yl) ** 2 <= R ** 2
    
    cnt = 0
  
    for row in range(max(y1, yl - R), min(y2, yl + R) + 1):
        left, right = xl - R, xl
        while left < right:
            mid = (left + right) // 2
            if not inside(mid, row):
                left = mid + 1
            else:
                right = mid
        l = left

        left, right = xl, xl + R
        while left < right:
            mid = (left + right + 1) // 2
            if not inside(mid, row):
                right = mid - 1
            else:
                left = mid
        r = left
        
        # print(r, l)
        # print(min(r, x2), max(l, x1))

        cnt += min(r, x2) - max(l, x1) + 1
    return cnt


print(solution(0, 0, 1, 1, 0, -7, 8))
print(solution(0, 0, 2, 2, 0, 0, 3))
print(solution(-1,1,3,2,0,0,2))  # expected 4, my output 1



