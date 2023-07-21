class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            elif asteroid < 0:
                while stack and stack[-1] > 0:
                    prev = stack.pop()
                    s = prev + asteroid
                    if s == 0:
                        break
                    elif s > 0:
                        stack.append(prev)
                        break
                else:
                    stack.append(asteroid)
        return stack