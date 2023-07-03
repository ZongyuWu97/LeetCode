class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        pairs = list(zip(positions, healths, list(directions), list(range(n))))
        pairs.sort(key=lambda x:x[0])

        stack = []
        for i in range(n):
            current = pairs[i]
            if not stack:
                stack.append(current)
                continue
            
            if current[2] == 'R':
                stack.append(current)
                continue

            while stack and stack[-1][2] == 'R' and current[2] == 'L':
                tmp = stack.pop()
                if tmp[1] < current[1]:
                    current = (current[0], current[1] - 1, current[2], current[3])
                elif tmp[1] > current[1]:
                    current = (tmp[0], tmp[1] - 1, tmp[2], tmp[3])
                else:
                    current = None
                    break
            
            if current:
                stack.append(current)

        
        stack.sort(key=lambda x:x[3])
        return [x[1] for x in stack]
        
