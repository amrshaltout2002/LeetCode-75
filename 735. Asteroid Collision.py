class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                last = stack.pop()
                if last > -i:
                    stack.append(last)
                    break
                if last == -i:
                    break
            else:
                stack.append(i)
        return stack